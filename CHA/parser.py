import csv

lol = list(csv.reader(open('SubClasses', 'rb'), delimiter='\t'))

file=open("ImmediateSubclass.facts","w")

for i in range(len(lol)):
	for j in range (1,len(lol[i])):	
		s='\t'.join((lol[i][0],lol[i][j]))
		file.write(s+'\n')

file.close()




lol = list(csv.reader(open('Methods', 'rb'), delimiter='\t'))

file=open("Methods.facts","w")

for i in range(len(lol)):
	for j in range (1,len(lol[i])):	
		s='\t'.join((lol[i][0],lol[i][j]))
		file.write(s+'\n')

file.close()