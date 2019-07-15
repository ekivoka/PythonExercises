import json



#jsonStr = input()
jsonStr = '[{"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}, {"name": "A", "parents": []}, {"name": "D", "parents":["C", "F"]}, {"name": "E", "parents":["D"]}, {"name": "F", "parents":[]}]'

classList = json.loads(jsonStr)
classDict = dict()
for cl in classList:
    for p in cl["parents"]:
        if p not in classDict:
            classDict[p] = []
        classDict[p].append(cl["name"])
        if cl["name"] not in classDict:
            classDict[cl["name"]] = []
            
def countChilds(parent):
    n = 1 #A:A
    if parent in classDict:
        n += len(classDict[parent])
    return n


for p in classDict:
    print(p,':',countChilds(p))
