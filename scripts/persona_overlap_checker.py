import os
import json


def find_overlap(k,data,urls):
	
	total = len(urls) #its 20 for sure but just to be generic
	uncommon_urls = 0

	for url in urls:
		for v in data:
			key = list(v.keys())[0]
			if key == k:
				continue
			if url in v[key]:
				uncommon_urls += 1
				break


	return uncommon_urls

path = '../data/personas'
data = []
keys = []
for d in os.listdir(path):
	with open(os.path.join(path,d),'r') as file:
		x = json.load(file)
		data.append(x)
		keys.append(list(x.keys())[0])

res = {}
for item in data:
	k = list(item.keys())[0]
	res1 = find_overlap(k,data,item[k])
	res[k] = res1


with open("../stats/overlapped_persona_stats.txt",'w') as file:
	for k,v in res.items():
		file.write(str(k)+" : "+str(v)+" Url(s) are in atleast one other persona\n")