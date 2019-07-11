import sys
import re

def repl(m):
    return m.group(1)[1]+m.group(1)[0]+m.group(1)[2:]

lines = []

for line in sys.stdin:
    line = line.rstrip()
    lines.append(line)
       
    # process line
    
for line in lines:
    result = re.sub(r"(\b[a-zA-Z0-9]{2}[a-zA-Z0-9]*\b)",repl, line)
    print(result)
