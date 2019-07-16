import json



#jsonStr = input()
jsonStr = '[{"name": "A", "parents": ["B", "C", "D"]},{"name": "E", "parents": ["F", "G"]},{"name": "I", "parents": ["E", "F", "Y", "D", "G"]},{"name": "B", "parents": ["I", "Y", "D", "G"]},{"name": "F", "parents": ["D", "Z"]},{"name": "C", "parents": ["Y", "G", "Z"]},{"name": "Y", "parents": []},{"name": "D", "parents": []},{"name": "G", "parents": ["Y", "D"]},{"name": "Z", "parents": ["D", "G"]}]'
classList = json.loads(jsonStr)
classDict = dict()
for cl in classList:
    for p in cl["parents"]:
        if p not in classDict:
            classDict[p] = []
        classDict[p].append(cl["name"])
        if cl["name"] not in classDict:
            classDict[cl["name"]] = []
'''         
def childs(parent):
    ch = classDict[parent]
    
    if ch == []:
        return []
    result = ch
    for key in ch:
        result += childs(key)
        print(result)
    return result

def countChilds(parent):
    result = set()
    for key in childs(parent):
        if key not in result:
            result.add(key)
    return len(result)+1        
'''
    
def countChilds(parent):
    global ch
    ch = []
    childs(parent)    
    return len(ch)

def childs(parent):
    a = classDict[parent]
    if a!=[]:
        for key in a:
            if key not in ch:
                ch.append(key)
                childs(key)
     
    

ch = list()



list_keys = list(classDict.keys())
list_keys.sort()
for i in list_keys:
    print(i, ':', countChilds(i))

