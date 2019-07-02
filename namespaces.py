n = int(input())

nameSpaces = {'global':['global']}

def create(NS, parent):
    global nameSpaces
    nameSpaces[NS] = [parent]
    nameSpaces[parent].append(NS)
    return

def add(NS, var):
    global nameSpaces
    nameSpaces[var] = [NS]
    nameSpaces[NS].append(var)
    return
    
def get(NS, var):
    global nameSpaces
    if var in nameSpaces[NS][1:]:
        return NS
    elif NS == 'global':
        return None
    else:
        return(get(nameSpaces[NS][0], var))


for i in range(n):
    cmd, namesp, arg = input().split()
    if cmd == 'create':
        create(namesp, arg)
    if cmd == 'add':
        add(namesp, arg)
    if cmd == 'get':
        print(get(namesp, arg))
    print(nameSpaces)
