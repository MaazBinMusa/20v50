import os
import json
import csv
from matplotlib import pyplot as plt
import numpy as np

data = []
count = {}

with open('run1_2020-12-01_final.json','r') as file:
	data = json.load(file)

for item in data:
	url = item['img_url']
	if(item['img_hash'] == -1 or item['RTB'] == 0):
		continue
	cat = url.split("_")[3]
	url = int(url.split("_")[2])

	if(url not in count):
		count[url] = {}
	
	if(cat not in count[url]):
		count[url][cat] = 0
	count[url][cat] += 1


data1 = []
data2 = []
data3 = []
data4 = []
data5 = []
data6 = []
data7 = []

# for i in ["Control","Games","Adult","Health","Sports","News","Recreation"]:
# 	#print(i," :",count[5][i])
# 	#print(i," :",count[10][i])
# 	print(i," :",count[20][i])
# 	data1.append(count[20][i])
# 	#print(i," :",count[25][i])
# 	print(i," :",count[50][i])
# 	data2.append(count[50][i])
# 	print("------------------")

data1.append(count[20]["Control"])
data1.append(count[50]["Control"])
data2.append(count[20]["Games"])
data2.append(count[50]["Games"])
data3.append(count[20]["Adult"])
data3.append(count[50]["Adult"])
data4.append(count[20]["Health"])
data4.append(count[50]["Health"])
data5.append(count[20]["News"])
data5.append(count[50]["News"])
data6.append(count[20]["Recreation"])
data6.append(count[50]["Recreation"])
data7.append(count[20]["Sports"])
data7.append(count[50]["Sports"])

f, (ax1) = plt.subplots(1, figsize=(10,5))

## Absolute count

ax1.bar(range(len(data1)), data1, label='Control', alpha=0.5, color='b')
ax1.bar(range(len(data2)), data2, bottom=data1, label='Games', alpha=0.5, color='r')
ax1.bar(range(len(data3)), data3, bottom=np.array(data1)+np.array(data2), label='Adult', alpha=0.5, color='g')
ax1.bar(range(len(data4)), data4, bottom=np.array(data1)+np.array(data2)+np.array(data3), label='Health', alpha=0.5, color='c')
ax1.bar(range(len(data5)), data5, bottom=np.array(data1)+np.array(data2)+np.array(data3)+np.array(data4), label='News', alpha=0.5, color='m')
ax1.bar(range(len(data6)), data6, bottom=np.array(data1)+np.array(data2)+np.array(data3)+np.array(data4)+np.array(data5), label='Recreation', alpha=0.5, color='y')
ax1.bar(range(len(data7)), data7, bottom=np.array(data1)+np.array(data2)+np.array(data3)+np.array(data4)+np.array(data5)+np.array(data6), label='Sports', alpha=0.5, color='k')

plt.sca(ax1)
plt.xticks([0, 1],  ['20', '50'])
ax1.set_ylabel("Count")
ax1.set_xlabel("Sites Count")
plt.legend(loc='upper right')

plt.show()
