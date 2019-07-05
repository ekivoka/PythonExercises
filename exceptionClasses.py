def isParent(cl, parent):
    global CTree
    if cl in CTree:
        if parent in CTree[cl]:
            return True
        elif cl == parent:
            return True
        else:
            for node in CTree[cl]:
                res = isParent(node, parent)
                if res:
                    return True
    return False


CTree = dict()

ListClass = [
    'a',
    'b : a',
    'c : a',
    'f : a',
    'd : c b',
    'g : d f',
    'i : g',
    'm : i',
    'n : i',
    'z : i',
    'e : m n ',
    'y : z',
    'x : z',
    'w : e y x',
]

ListCheck = [
    'y',
    'm',
    'n',
    'm', 
    'd',
    'e',
    'g',
    'a',
    'f',
    
]


#n = int(input())
n = len(ListClass)

for i in range(n):
    
    #classMas = input().split(' ')
    classMas = ListClass[i].split(' ')
    
    className = classMas[0]
    parents = classMas[2:]
    if className not in CTree:
        CTree[className] = []
    CTree[className]+=parents

#n = int(input())
n = len(ListCheck)
classMas = []
bads = []
for i in range(n):
    #classMas.append(input())
    classMas.append(ListCheck[i])
classMas = classMas[::-1]
answer = []
for i in range(n):
    for j in range(i+1,n):
        #print('i',classMas[i])
        #print('j',classMas[j])
        if isParent(classMas[i], classMas[j]):
            if classMas[i] not in bads:
                answer.append(classMas[i])
                bads.append(classMas[i])
for key in answer[::-1]:
    print(key)

    
