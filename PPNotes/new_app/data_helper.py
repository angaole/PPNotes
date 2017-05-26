import json

def getNodes(arg):
    fin = open(arg, 'r')
    line = fin.readline()
    line = fin.readline()
    nodes = []
    while line:
        data = {"category":0, "name":line.split("\t", 1)[0]}
        jsondata = json.dumps(data)
        nodes.append(jsondata)
        line = fin.readline()
    return nodes

def getLinks(arg):
    fin = open(arg, 'r')
    line = fin.readline()
    line = fin.readline()
    links = []
    while line:
        lis = line.split("\t")
        links.append([lis[0], lis[1], lis[2]])
        line = fin.readline()
    return links
