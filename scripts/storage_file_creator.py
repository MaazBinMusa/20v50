import os
import json

storage_file_path = '../automation/DeployBrowsers/firefox_extensions/ublock_origin'
os.chdir('../ent_abp')

default_storage_file = {}
with open(os.path.join(storage_file_path,'storage.js'),'r') as file:
	default_storage_file = file.read()
	default_storage_file = json.loads(default_storage_file)

for d in os.listdir('.'):
	key = d.replace('.txt','')
	temp   = default_storage_file
	with open(os.path.join(storage_file_path,'storage_{}.js'.format(key)),'w') as file:
		temp['selectedFilterLists'] = []
		temp['selectedFilterLists'].append(key)
		temp['availableFilterLists'][key] = {"content":"filters","group":"default","title":key,"contentURL":["assets/ublock/{}.txt".format(key)]}
		json.dump(default_storage_file,file)

