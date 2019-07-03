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

n = int(input())

for i in range(n):
    
    classMas = input().split(' ')
    className = classMas[0]
    parents = classMas[2:]
    
    

    if className not in CTree:
        CTree[className] = []
    CTree[className]+=parents
    print(CTree)

n = int(input())

for i in range(n):
    
    parent, cl = input().split(' ')

    #определяем является ли класс родителем
    if isParent(cl, parent):
        print('Yes')
    else:
        print('No')
    

    

