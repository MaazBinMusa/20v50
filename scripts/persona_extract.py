from bs4 import BeautifulSoup
import os
import requests
import tldextract
import time
import json
# res = tldextract.extract(url)
# tld = res.domain
# sub = res.subdomain

keys = ["Adult",
"Games",
"Health",
"News",
"Recreation",
"Sports"]




urls = {}
for key in keys:
	urls[key] = []
	url = "https://www.alexa.com/topsites/category/Top/{}".format(key)
	print(url)
	r = requests.get(url)
	soup = BeautifulSoup(r.content, "html.parser")
	
	ans1 = soup.find_all("div",class_="DescriptionCell")
	for ans in ans1:
		a = ans.find("a")
		urls[key].append(a['href'])
	time.sleep(3)

with open("../data/cmb.json",'w') as file:
	json.dump(urls,file)


processed = {}
with open("../data/cmb.json",'r') as file:
	processed = json.load(file)

comb = {}
urls = {}
for k,v in processed.items():
	if k not in urls:
		urls[k] = []
	for url in v:
		url = url.replace("/siteinfo/","")
		res = tldextract.extract(url)
		if(res.domain not in comb):
			urls[k].append("http://www."+url)
		comb[res.domain] = 1

# for k,v in urls.items():
# 	print(k,": ",len(v))
for k,v in urls.items():
	d = {}
	d[k] = v
	with open("../data/personas/"+k+".json",'w') as file:
		json.dump(d,file)