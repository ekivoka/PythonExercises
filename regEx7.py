# put your python code here
import sys
import re


lines = []

for line in sys.stdin:
    line = line.rstrip()
    lines.append(line)
       
    # process line
    
for line in lines:
    result = re.sub(r'(\b\S*a\b)', 'argh', line,count=1, flags=re.IGNORECASE)
    print(result)
