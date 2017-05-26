import json

categorylist = [{"name":'point'}]
fin = open("./pink_node.txt", 'r')
line = fin.readline()
line = fin.readline()
nodelist = []
nodedict = dict()
while line:
    nodename = line.split("\t", 1)[0]
    nodelist.append({"category":0, "name":nodename})
    nodedict[nodename] = len(nodedict)
    line = fin.readline()
    
fin = open("./pink_edge.txt", 'r')
line = fin.readline()
line = fin.readline()
linklist = []
while line:
    lis = line.split("\t")
    source = nodedict[lis[0]]
    target = nodedict[lis[1]]
    weight = float(1)/float(lis[2])
    linklist.append({"source":source, "target":target, "weight":weight})
    line = fin.readline()

data = {"category":categorylist, "nodes":nodelist, "links":linklist}
fout = open("data.json", 'w')
fout.write(json.dumps(data))
