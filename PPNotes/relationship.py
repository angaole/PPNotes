import json

categorylist = [{"name":'point'}]
fin = open("./pink_node.txt", 'r')
fout = open("data0.json", 'w')
line = fin.readline()
line = fin.readline()
nodelist = []
nodedict = dict()
while line and line!="\n":
    nodename = line.split("\t", 1)[0]
    fout.write('{category:0, name:"'+nodename+'"},'+" ")
    line = fin.readline()
fout.write("\n")
fin = open("./pink_edge.txt", 'r')
line = fin.readline()
line = fin.readline()
linklist = []
while line:
    lis = line.split("\t")
    source = lis[0]
    target = lis[1]
    fout.write('{source:"'+source+'", target:"'+target+'", weight:1},'+" ")
    line = fin.readline()
