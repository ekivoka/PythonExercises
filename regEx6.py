import sys
import re


lines = []

for line in sys.stdin:
    line = line.rstrip()
    lines.append(line)
       
    # process line
    
for line in lines:
    result = re.sub(r'human', 'computer', line)
    print(result)
