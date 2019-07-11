# put your python code here

import sys
import re


lines = []

for line in sys.stdin:
    line = line.rstrip()
    lines.append(line)
       
    # process line
    
for line in lines:
    result = re.findall(r'\bcat\b', line)
    if len(result)>0:
        print(line)
