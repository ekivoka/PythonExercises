# put your python code here
import sys
import re

lines = []
string = "text"
for line in sys.stdin:
    line = line.rstrip()
    lines.append(line)
       
    # process line
    
for line in lines:
    res = re.fullmatch(r"(0|1(01*0)*1)*",line)
    if res and res.group(0):
            print(line)
