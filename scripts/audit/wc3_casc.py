"""Минимальный доступ к CASC Warcraft III через CascLib.dll из HiveWE."""
import ctypes
import os
from ctypes import wintypes

DLL_DIR = r'F:\WARCRAFT III\WARCRAFT_SOFT\HiveWE'
os.add_dll_directory(DLL_DIR)
lib = ctypes.WinDLL(os.path.join(DLL_DIR, 'CascLib.dll'))
lib.CascOpenStorage.argtypes = [ctypes.c_wchar_p, wintypes.DWORD, ctypes.POINTER(ctypes.c_void_p)]
lib.CascOpenStorage.restype = wintypes.BOOL
lib.CascOpenFile.argtypes = [ctypes.c_void_p, ctypes.c_void_p, wintypes.DWORD, wintypes.DWORD, ctypes.POINTER(ctypes.c_void_p)]
lib.CascOpenFile.restype = wintypes.BOOL
lib.CascGetFileSize.argtypes = [ctypes.c_void_p, ctypes.POINTER(wintypes.DWORD)]
lib.CascGetFileSize.restype = wintypes.DWORD
lib.CascReadFile.argtypes = [ctypes.c_void_p, ctypes.c_void_p, wintypes.DWORD, ctypes.POINTER(wintypes.DWORD)]
lib.CascReadFile.restype = wintypes.BOOL
lib.CascCloseFile.argtypes = [ctypes.c_void_p]


lib.CascFindFirstFile.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p, ctypes.c_wchar_p]
lib.CascFindFirstFile.restype = ctypes.c_void_p
lib.CascFindNextFile.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
lib.CascFindNextFile.restype = wintypes.BOOL
lib.CascFindClose.argtypes = [ctypes.c_void_p]


class Casc:
    def __init__(self, root=r'F:\Games\Warcraft III'):
        self.h = ctypes.c_void_p()
        if not lib.CascOpenStorage(root, 0, ctypes.byref(self.h)):
            raise OSError('CascOpenStorage failed: %d' % ctypes.GetLastError())
        # промах при открытии по имени стоит секунды, поэтому сначала собираем индекс имён
        self.names = {}
        buf = ctypes.create_string_buffer(4096)
        # все слои игры (_hd, _de, _locales, _tilesets, _teen, _deprecated) вложены в war3.w3mod
        hf = lib.CascFindFirstFile(self.h, b'war3.w3mod:*', buf, None)
        while hf:
            n = buf.raw[:260].split(b'\0', 1)[0].decode('latin1')
            self.names.setdefault(n.lower(), n)
            if not lib.CascFindNextFile(hf, buf):
                break
        if hf:
            lib.CascFindClose(hf)

    def read(self, name):
        hf = ctypes.c_void_p()
        if not lib.CascOpenFile(self.h, name.encode('utf-8'), 0, 0, ctypes.byref(hf)):
            return None
        try:
            hi = wintypes.DWORD()
            size = lib.CascGetFileSize(hf, ctypes.byref(hi))
            buf = ctypes.create_string_buffer(size)
            got = wintypes.DWORD()
            lib.CascReadFile(hf, buf, size, ctypes.byref(got))
            return buf.raw[:got.value]
        finally:
            lib.CascCloseFile(hf)

    def find(self, path):
        """Классический путь игры (Textures\\Footman.blp) → байты из SD-архива или None."""
        p = path.replace('/', '\\')
        stem = os.path.splitext(p)[0]
        for name in ('war3.w3mod:' + p, 'war3.w3mod:' + stem + '.blp', 'war3.w3mod:' + stem + '.dds',
                     'war3.w3mod:_hd.w3mod:' + stem + '.dds'):
            name = self.names.get(name.lower())
            if not name:
                continue
            data = self.read(name)
            if data:
                return name, data
        return None, None


if __name__ == '__main__':
    c = Casc()
    for t in ('Textures\\Footman.blp', 'Textures\\HeroArthas.blp', 'units\\human\\Footman\\Footman.mdx'):
        n, d = c.find(t)
        print(t, n, len(d) if d else None, d[:4] if d else None)
