from multi import process_docker
from multi import collect_ads
import multiprocessing
import os
from os import system
import time

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
		sets.append('_'.join([i,j]))

#for i in range(16):
#	sets.append('Test_NoIntent')

#sets = ['Test_NoIntent']


start = 1
end   = 101
for s in sets:
	# creating processes
	p1 = multiprocessing.Process(target=collect_ads, args=(s,range(1,26)))
	p2 = multiprocessing.Process(target=collect_ads, args=(s,range(26,51)))
	p3 = multiprocessing.Process(target=collect_ads, args=(s,range(51,76)))
	p4 = multiprocessing.Process(target=collect_ads, args=(s,range(76,101)))
	p1.start()
	p2.start()
	p3.start()
	p4.start()
	time.sleep(10)
