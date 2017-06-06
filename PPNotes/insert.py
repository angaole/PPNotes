import MySQLdb

conn = MySQLdb.connect(host='localhost', user='root', passwd='Workhard0407')
cursor = conn.cursor()
cursor.execute("use mydata;")
'''
fin = open("./message_dis_snp", 'r')
line = fin.readline().replace("hahasnpsnpid", "hahasnp\tsnpid")
number = 1
while line:
    lists = line[:-1].split("\t")
    # print lists
    string = str(number)+ ",'"+lists[0]+"','"+lists[1]+"','"+lists[2]+"','"+lists[3]+"','"+lists[4]+"','"+lists[5]+"','"+lists[6]+"'"
    # print string
    cursor.execute("insert into new_app_messa value("+string+");")
    number += 1
    line = fin.readline().replace("hahasnpsnpid", "hahasnp\tsnpid")
'''
fin = open("./expre_seq", 'r')
line = fin.readline()
while line:
    expre = fin.readline()[1:-1]
    seq = fin.readline()[:-1]
    lists = line[:-1].split("\t")
    string = "'"+lists[0]+"','"+lists[1]+"','"+expre+"','"+seq+"','"+lists[3]+"','"+lists[5]+"','"+lists[4]+"','"+lists[2]+"'"
    print string
    cursor.execute("insert into new_app_seqe value("+string+");")
    line = fin.readline()
'''
fin = open("./gene", 'r')
line = fin.readline()
number = 1
while line:
    lists = line[:-1].split("\t")
    string = str(number)+",'"+lists[0]+"','"+lists[1]+"','"+lists[2]+"'"
    cursor.execute("insert into new_app_genes value("+string+");")
    number += 1
    line = fin.readline()
'''
conn.commit()
cursor.close()
