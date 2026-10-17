"""Reproduce the patched headless CLI in the repository cache, without changing installed HiveWE."""
import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from wc3_project import ROOT, CACHE, read


def command(args, name, cwd=ROOT):
    CACHE.mkdir(parents=True, exist_ok=True)
    log = CACHE / f"hivewe-{name}.log"
    print(f"{name}: {log}", flush=True)
    with log.open("w", encoding="utf-8") as output:
        proc = subprocess.run([str(a) for a in args], cwd=cwd, stdout=output, stderr=subprocess.STDOUT)
    if proc.returncode:
        raise RuntimeError(f"{name} failed ({proc.returncode}); see {log}")


def checkout(url, directory, revision):
    if not directory.exists():
        command(["git", "clone", "--depth", "1", url, directory], "clone-" + directory.name)
    head = subprocess.check_output(["git", "-C", str(directory), "rev-parse", "HEAD"], text=True).strip()
    if head != revision:
        changes = subprocess.check_output(["git", "-C", str(directory), "status", "--porcelain"], text=True)
        if changes:
            raise RuntimeError(f"Cannot change revision of dirty checkout: {directory}")
        command(["git", "-C", directory, "fetch", "origin", revision, "--depth", "1"], "fetch-" + directory.name)
        command(["git", "-C", directory, "checkout", "--detach", revision], "checkout-" + directory.name)


def activate(executable):
    path = ROOT / "wc3.local.json"
    config = json.loads(read(path)) if path.exists() else {}
    config["cli"] = str(executable.resolve())
    path.write_text(json.dumps(config, ensure_ascii=False, indent=2), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--activate", action="store_true", help="Select tested CLI in wc3.local.json")
    parser.add_argument("--verify-only", action="store_true", help="Verify an already built CLI")
    args = parser.parse_args()
    source, deps, build = ROOT / ".cache/hivewe-source", ROOT / ".cache/vcpkg", ROOT / ".cache/hivewe-build"
    executable = build / "Release/HiveWE_cli.exe"
    try:
        if not args.verify_only:
            checkout("https://github.com/VinerX/HiveWE.git", source, read(ROOT / "patches/hivewe-base.txt").strip())
            checkout("https://github.com/microsoft/vcpkg.git", deps, read(ROOT / "patches/vcpkg-base.txt").strip())
            patch = ROOT / "patches/hivewe-cli.patch"
            already = subprocess.run(["git", "-C", str(source), "apply", "--reverse", "--check", str(patch)],
                                     capture_output=True).returncode == 0
            if not already:
                command(["git", "-C", source, "apply", "--check", patch], "patch-check")
                command(["git", "-C", source, "apply", patch], "patch-apply")
            if not (deps / "vcpkg.exe").exists():
                command([deps / "bootstrap-vcpkg.bat", "-disableMetrics"], "bootstrap")
            command([deps / "vcpkg.exe", "install", "glm", "abseil", "bzip2", "stormlib", "casclib",
                     "nlohmann-json", "unordered-dense", "--classic", "--triplet", "x64-windows",
                     "--overlay-ports=" + str(source / "overlay-ports"), "--disable-metrics"], "dependencies")
            cmake = shutil.which("cmake") or str(Path("C:/Program Files (x86)/Microsoft Visual Studio/2022/BuildTools") /
                                                "Common7/IDE/CommonExtensions/Microsoft/CMake/CMake/bin/cmake.exe")
            command([cmake, "-S", source, "-B", build, "-G", "Visual Studio 17 2022", "-A", "x64",
                     "-DHIVEWE_CLI_ONLY=ON", "-DVCPKG_MANIFEST_MODE=OFF",
                     "-DCMAKE_TOOLCHAIN_FILE=" + str(deps / "scripts/buildsystems/vcpkg.cmake"),
                     "-DVCPKG_TARGET_TRIPLET=x64-windows"], "configure")
            command([cmake, "--build", build, "--config", "Release", "--target", "HiveWE_cli", "--parallel", "2"], "build")
        proc = subprocess.run([str(executable), "capabilities"], capture_output=True, text=True, encoding="utf-8")
        capabilities = json.loads(proc.stdout)
        if proc.returncode or capabilities.get("schema_version") != 1 or not capabilities.get("features", {}).get("validate_map"):
            raise RuntimeError("Patched CLI capability contract failed")
        with tempfile.TemporaryDirectory(prefix="hivewe-contract-", dir=CACHE) as temporary:
            root = Path(temporary)
            folder = root / "map"; folder.mkdir()
            (folder / "war3map.lua").write_text("function main() end\nfunction config() end\n", encoding="utf-8")
            shutil.copy2(ROOT / "map.w3x/war3map.w3i", folder / "war3map.w3i")
            archive = root / "probe.w3x"
            proc = subprocess.run([str(executable), "build-map", "--map", str(folder), "--out", str(archive)],
                                  capture_output=True, text=True, encoding="utf-8")
            packaged = json.loads(proc.stdout)
            if proc.returncode or packaged.get("files_added") != 2 or not archive.exists() or archive.stat().st_size == 0:
                raise RuntimeError("MPQ roundtrip contract failed; check the StormLib Unicode overlay")
        if args.activate:
            activate(executable)
        print(json.dumps({"ok": True, "cli": str(executable), "activated": args.activate}, ensure_ascii=False))
        return 0
    except (OSError, RuntimeError, ValueError, subprocess.CalledProcessError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
