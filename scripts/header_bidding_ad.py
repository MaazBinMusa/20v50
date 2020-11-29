## TestProfile
	## persona_1
		## .html
		## .html
	## persona_n
		## .html
		## .html
## ControlProfile
	## persona_1
		## .html
		## .html
	## persona_n
		## .html
		## .html
## c.py

import os
import re
import json
import time
import urllib2

def extract_item(name,data,end_delim=[", ","}}"]):
	
	val = "not found"
	for i in range(len(data)):
		cap = ""
		dis = len(name)+4
		if(data[i:i+dis] == "'{}': ".format(name)):
			#print(data[i:i+dis])
			for j in range(i+dis, len(data)):
				if(data[j:j+2] == end_delim[0] or data[j:j+2] == end_delim[-1]):
					val = cap
					break
				cap += data[j]
		if(val != "not found"):
			break
	return val

def extract_urls(name,data,end_delim=['" ','">','><']):
	
	val = []
	for i in range(len(data)):
		cap = ""
		dis = len(name)
		if(data[i:i+dis] == "{}".format(name)):
			#print(data[i:i+dis])
			for j in range(i+dis, len(data)):
				if(data[j:j+2] == end_delim[0] or data[j:j+2] == end_delim[1] or data[j:j+2] == end_delim[2]):
					tmp = cap
					val.append(tmp.strip("/").strip("\\").strip('"').strip("/").strip("\\"))
					break
				cap += data[j]
	return val

def extract_ad_html(_str):
	
	ads = []
	for i in range(len(_str)):
			cap = ""
			if(_str[i:i+8] == "'ad': u'"):
				for j in range(i+8, len(_str)):
					if(_str[j:j+4] == "', u"):
						ads.append(cap)
						break
					cap += _str[j]
	new_ads = []
	for i in range(len(ads)):
		if(len(ads[i]) > 25):
			new_ads.append(ads[i])
	
	if(len(new_ads) > 0):
		return new_ads[0]
	return -1

def clean_json(data):

	return data.replace("u\\'","'").replace("\\'","'").replace("b'\\n","").replace(": True",": 'True'").replace(": False",": 'False'").replace(": None",": 'None'")

def process_ad(res,path,ssd):
	sd = path.split("/")[-1]
	with open(os.path.join(path,ssd),'r') as ad:
		ads = []
		data = str(ad.read().encode('UTF-8'))
		
		## Preprocessing
		## Preprocessing

		data2 = data.split("}} ")
		data3 = []
		for item in data2[:-1]:
			data3.append(item+"}} ")
		data3.append(data2[-1])
		data2 = data3
		data3 = []
		for item in data2:
			data3.append(clean_json(item))
		data2 = data3

		## data2 now has list of ad jsons as strings
		## data2 now has list of ad jsons as strings
		
		index = 1
		for item in data2:
			ad_html = extract_ad_html(item)

			if(ad_html != -1):

				key = sd+'_'+str(index)
				res[key] = {}
				index += 1

				val  = extract_urls('img src=',item)
				val2 = extract_urls('a href=',item)
				res[key]['ad_html'] = ad_html
				res[key]['urls']	= val + val2

				
				

				extract_items 		= ["cpm","bidder","originalCurrency","pbHg","pbLg","pbCg","pbMg","pbAg","pbDg","currency","height","size","width","mediaType","bidderCode","originalCpm","statusMessage"]
				for i in extract_items:
					res[key][i]		= extract_item(i,item)

		return res
				
		
		

		
def start(path):

	mode = True
	res  = {}
	import os
	if(mode):
		#path  = '.'
		for ssd in os.listdir(path):
			if('Header_Bidding' in ssd):
				#print(sd)
				res = process_ad(res,path,ssd)
				for k,v in res.items():
					with open(path+'/{}.json'.format(k),'w') as file:
						json.dump(v, file, ensure_ascii=False, indent=3)
					with open(path+'/{}.html'.format(k),'w') as file:
						file.write(v['ad_html'])
				res = {}

		
def cap_images(path,driver):
	
	import os

	for item in os.listdir(path): #for htmls
		try:
			if("html" not in item):
				continue
			print(item)
			html_file = os.path.join(os.getcwd(),path,item)

			driver.get("file:///"+html_file)
			time.sleep(1)
			item_t = item.replace(".html","")
			driver.get_screenshot_as_file(path+"/{}.png".format(item_t))
		
		except Exception as e:
			with open(path+'/{}_error.txt'.format(item_t),'w') as file:
				file.write(str(e))


	for item in os.listdir(path): #for urls

		if("json" not in item or 'RTB' in item):
			continue
		print(item)

		json_file = os.path.join(path,item)
		with open(json_file,'r') as file:
			data = json.load(file)
			index2 = 1

			for url in data["urls"]:
				url = url.strip("'")
				url = url.strip("'")
				for i in range(10):
					url = url.strip("\\")
				try:
					site = url
					request = urllib2.Request(site,headers={'User-Agent':'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 firefox/2.0.0.11'})
					page = urllib2.urlopen(request)
					item_t = item.replace(".json","")
					file_name = "/{}_url_{}.png".format(item_t,str(index2))
					with open(path+"/{}.png".format(file_name),'wb') as f:
						f.write(page.read())
					time.sleep(2)
						
				except Exception as e:
					print("Error")
					with open(path+"/error_{}_url_{}.txt".format(item_t,str(index2)),'w') as file:
						file.write(str(e))
				index2 += 1

		#driver.quit()
