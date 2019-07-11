import requests
import re

A = "http://pastebin.com/raw/2mie4QYa"
B = "stepic.org/media/attachments/lesson/24472/sample2.html"








html = "<a href=\"http://stepic.org/courses\"> <a href=\'https://stepic.org\'><a href=\'http://neerc.ifmo.ru:1345\'><a href=\"ftp://mail.ru/distib\" ><a href=\"ya.ru\"><a href=\"www.ya.ru\"><a href=\"../skip_relative_links\">"
    
#"linkPattern = r"<a [0-9a-zA-Z]*href=[\"\'](https://([\w.:]*).*)\">"
# put your python code here


html = requests.get(A).text

linkPattern=r"(<a .*href=[\"\'](https|http|ftp)?://)([\w.\-_]*)(.*a>)?"

Links = re.findall(linkPattern, html)

res = []
for l in Links:
    if l[2] not in res:
        res.append(l[2])
        
res.sort()

for r in res:
    print(r)
