
fr = open("D:\\03-Study\\Python\\test\\content.txt", "r+")

for line in fr.readlines():
    index = line.find("\t")
    print line[0:index]
    

