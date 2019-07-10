# put your python code here
s = input()
t = input()
n = 0
for i in range(len(s)):
    if s[i:].startswith(t):
        n+=1
print(n)
