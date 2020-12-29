import os
import json
import csv
from matplotlib import pyplot as plt
import numpy as np

data = []
count = {}

with open('run2_2020-12-28_final.json','r') as file:
	data = json.load(file)

for item in data:
	
	url = item['img_url']
	hash_ = item['img_hash']

	cat = url.split("_")[3]
	num = int(url.split("_")[2])

	if(num not in count):
		count[num] = {}
	
	if(cat not in count[num]):
		count[num][cat] = []
	count[num][cat].append(hash_)


for k in [5,10,15,20,25,50,75,100]:
	print(k)
	print(len(set(count[k]['All'])))
	print("-----------")