from multi import process_docker
from multi import collect_ads
import multiprocessing
import os
from os import system


p1 = []
p2 = ['Intent','NoIntent']

for d in os.listdir('../data/personas/'):
	part = d.split('.json')[0]
	if part not in p1:
		p1.append(part)

# print(p1)
# print(p2)
sets = []

for i in p1:
	for j in p2:
		if j == 'NoIntent' and i == 'Control':
			continue
		sets.append('_'.join([i,j]))
#print(sets)
#exit()

for s in sets:

    # creating processes 
    #pt = multiprocessing.Process(target=process_docker, args=(s,range(1,2)))
    #pt.start()
    #break

    p1 = multiprocessing.Process(target=process_docker, args=(s,range(1,26))) 
    p2 = multiprocessing.Process(target=process_docker, args=(s,range(26,51)))
    p3 = multiprocessing.Process(target=process_docker, args=(s,range(51,76))) 
    p4 = multiprocessing.Process(target=process_docker, args=(s,range(76,101)))
    p1.start() 
    p2.start()
    p3.start() 
    p4.start()
