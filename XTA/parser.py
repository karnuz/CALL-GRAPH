import csv

lol = list(csv.reader(open('SubClasses', 'rb'), delimiter='\t'))

file=open("ImmediateSubclass.facts","w")

for i in range(len(lol)):
    for j in range (1,len(lol[i])): 
        s='\t'.join((lol[i][0],lol[i][j]))
        file.write(s+'\n')

file.close()


lol = list(csv.reader(open('Instantiated', 'rb'), delimiter='\t'))

file=open("Instantiated.facts","w")

for i in range(len(lol)):
    for j in range (2,len(lol[i])): 
        s='\t'.join((lol[i][0],lol[i][1],lol[i][j]))
        file.write(s+'\n')

file.close()

lol = list(csv.reader(open('Methods', 'rb'), delimiter='\t'))

file=open("Methods.facts","w")

for i in range(len(lol)):
    for j in range (1,len(lol[i])): 
        s='\t'.join((lol[i][0],lol[i][j]))
        file.write(s+'\n')

file.close()



lol = list(csv.reader(open('ParamTypes', 'rb'), delimiter='\t'))

file=open("ParamTypes.facts","w")

for i in range(len(lol)):
    for j in range (2,len(lol[i])): 
        s='\t'.join((lol[i][0],lol[i][1],lol[i][j]))
        file.write(s+'\n')

file.close()



lol = list(csv.reader(open('ReturnType', 'rb'), delimiter='\t'))

file=open("ReturnType.facts","w")

for i in range(len(lol)):
    for j in range (2,len(lol[i])): 
        s='\t'.join((lol[i][0],lol[i][1],lol[i][j]))
        file.write(s+'\n')

file.close()