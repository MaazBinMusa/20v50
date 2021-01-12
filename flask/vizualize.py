import os
import json
import csv
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

data = []
count = {}

with open('run3_2020-12-30_final.json','r') as file:
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
PersonaSize = [5,10,15,20,25,50,75,100]

for k in PersonaSize:
	print(k)
	print(len(set(count[k]['All'])))
	print("-----------")
	UniqueAds.append(len(set(count[k]['All'])))


data = {'PersonaSize':PersonaSize,'UniqueAds':UniqueAds}
df = pd.DataFrame(data)

# fig1 = sns.barplot(x='PersonaSize', y='UniqueAds', data = df, palette='summer')
# fig1.figure.savefig("check1.png")
fig2 = sns.lineplot(x='PersonaSize', y='UniqueAds', data = df, color='tab:red')
fig2.figure.savefig("check2.png")

# fig, ax1 = plt.subplots(figsize=(10,6))
# color = 'tab:green'

# #bar plot creation
# ax1.set_title('Unique Ads by Persona Size', fontsize=16)
# ax1.set_xlabel('Persona Size', fontsize=16)
# ax1.set_ylabel('Unique Ads', fontsize=16)
# ax1 = sns.barplot(x='PersonaSize', y='UniqueAds', data = df, palette='summer')
# ax1.tick_params(axis='y')

# #specify we want to share the same x-axis
# ax2 = ax1.twinx()
# color = 'tab:red'

# #line plot creation
# ax2 = sns.lineplot(x='PersonaSize', y='UniqueAds', data = df, color=color)
# ax2.tick_params(axis='y', color=color)

# #show plot
# print("Plt")
# plt.show()
# plt.savefig("check.png")