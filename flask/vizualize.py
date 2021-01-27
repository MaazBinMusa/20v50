import os
import json
import csv
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

data = []
count = {}
x = []

# x = [ [persona name, site num, val] , [persona name, site num, val] , [persona name, site num, val] ]

with open('run4_2021-01-24_final.json','r') as file:
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


UniqueAds = []
PersonaSize = [5,10,15,20,25,50]
PersonaCaty = ["Sports","Games","Health","Adult","Recreation","News"]

for personacat in PersonaCaty:
	for personasize in PersonaSize:
		x.append([personacat,personasize,len(set(count[personasize][personacat]))])


df = pd.DataFrame(x,columns=['sites','persona','unique ads'])

df.pivot("sites", "persona", "unique ads").plot(kind='bar',figsize=(15,10))

plt.savefig("check.png")