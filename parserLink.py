import requests
import re

A = requests.get("https://stepic.org/media/attachments/lesson/24472/sample1.html")
B = "stepic.org/media/attachments/lesson/24472/sample2.html"

def findLink(A, B):
    if A.status_code == 400:
        return False
    html = A.text
    
    linkPattern = r"<a [0-9a-zA-Z]*href=\"(.*)\">"
    Links = re.findall(linkPattern, html)
    
    for l in Links:
        res = requests.get(l)
        if res.status_code == 200 and B in res.text:
            return True
            
    return False   

if findLink(A, B):
    print('Yes')
else:
    print('No')
    
