
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('C:/Users/hirot/Desktop/DiscordBot/main.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")

# Find board section start and end  
start_line = None
end_line = None

for i, line in enumerate(lines):
    if '    """' in line and i > 12000 and i < 12010 and start_line is None:
        start_line = i
    if 'セクション 18' in line and start_line is not None:
        end_line = i
        break

print(f"Board start: {start_line}, end: {end_line}")

# Also search for the remnant orphaned docstring
for i, line in enumerate(lines[12000:12010], start=12001):
    print(f"{i}: {repr(line[:80])}")
