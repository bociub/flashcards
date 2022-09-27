import json, re

with open("szotarazott.txt", "r", encoding='utf-8') as file:
    thedict = {}
    for line in file:
        line = line.rstrip()
        if line == "":
            continue
        
        #x = line.split(",",1)
        x = re.split(',|- ', line)
        if len(x) != 2:
            continue
        thedict[x[0]] =  x[1]
      
x = json.dumps(thedict)

f = open("dictjson.txt", "w")
f.write(x)
f.close()
