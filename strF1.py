s = input()
a = input()
b = input()

n = 0

while True:
    if n > 1000:
        print('Impossible')
        break
    if a in s:
        s = s.replace(a,b)
        n += 1
    else:
        print(n)
        break
        
