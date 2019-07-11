# put your python code here

import sys
import re


lines = []

for line in sys.stdin:
    line = line.rstrip()
    lines.append(line)
    # process line
    
for line in lines:
    result = re.findall(r'cat', line)
    if len(result)>1:
        print(line)
