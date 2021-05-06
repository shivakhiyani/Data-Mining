# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import time
start_time = time.time()
fileToWrite = "kosarak.arff"
relation = "news"

data = []
maxEle = 0


writeFile = open(fileToWrite, 'w')
writeFile.write("@relation " + 'newsclick' + "\n\n")

with open('kosarak.dat', 'r') as f:
    d = f.readlines()

    for i in d:
        k = i.rstrip().split(" ")
        line = {int(ele) for ele in k}
        if max(line) > maxEle:
            maxEle = max(line)
        data.append(sorted(line))
#rows = len(data)
#print(maxEle)

#print(data)
writeFile.write('@attribute news' + str(0)+' '+ '{0,1}\n')
for m in range (1,maxEle+1):
     writeFile.write('@attribute news' + str(m) + ' ' + '{0,1}\n')

writeFile.write("\n@data\n")

for line in data:
    s = ''
    s = s + '{'
    for ele in line:
        s = s + str(ele) + ' ' + '1,'
    s = s[:-1]
    s = s + '}'
    writeFile.write(s+'\n')
print("--- %s seconds ---" % (time.time() - start_time))



    #l=[el for el in line +''+ 1]
    #print(l)
    #writeFile.write([el for el in line +''+ 1] +"\n")


