"""Replace null with nil in all Lua section files."""
import re
from pathlib import Path

SECTIONS_DIR = Path(r"C:\Games\23 Race\23-Race_Legion_Worktree3\map.w3x\_lua\monolith_split\sections")


def replace_null_in_line(line):
    """Replace standalone 'null' with 'nil'.
    Skip pure comment lines (starting with whitespace then --).
    For inline comments, changing null->nil is harmless.
    """
    if re.match(r'^\s*--', line):
        return line
    return re.sub(r'\bnull\b', 'nil', line)


def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    count = content.count('null')
    if count == 0:
        return 0
    
    lines = content.split('\n')
    new_lines = [replace_null_in_line(line) for line in lines]
    
    new_content = '\n'.join(new_lines)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return count


def main():
    total = 0
    for filepath in sorted(SECTIONS_DIR.rglob('*.lua')):
        count = process_file(filepath)
        if count:
            print(f"  {filepath.relative_to(SECTIONS_DIR)}: {count} replacements")
            total += count
    
    print(f"\nTotal replacements: {total}")


if __name__ == '__main__':
    main()
