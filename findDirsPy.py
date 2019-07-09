import os.path

cats = []  
for curdir, dirs, files in os.walk("main"):
    for file in files:
        if file[-3:] == '.py':
           if curdir not in cats:
               cats.append(curdir)

cats.sort()
answer = '\n'.join(cats)
f = open("main_ans.txt", "w")
f.write(answer)
f.close()
