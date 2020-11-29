import os
import json
import sys

personas_path = "../data/personas"
phase = "20_50"
data = {}

d_browser_param = json.loads(open('../automation/default_browser_params.json','r').read())
d_manager_param = json.loads(open('../automation/default_manager_params.json','r').read())


for file in os.listdir(personas_path):
	f = open(os.path.join(personas_path,file),'r').read()
	d = json.loads(f)
	data[file.replace('.json','')] = d[list(d.keys())[0]]

for nsites in [5,10,15,20,25,50]:
	new_data = {}
	for cat in data:
		new_data[cat] = data[cat][:nsites]

	NUM = 10

	for persona_name,value in new_data.items():

		temp = os.path.join('../config/{}'.format(phase),persona_name)
		if(not os.path.exists(temp)):
			os.makedirs(temp)


		sites = value

		i = 1
		while i <= NUM:

			with open(os.path.join(temp,'{}_{}_browser_params_{}.json'.format(nsites,persona_name,str(i))),'w') as json_file:
				t_browser_param 				      = d_browser_param
				t_browser_param["Persona_Path"]		  = "data/personas"
				t_browser_param["profile_archive_dir"]= "data/{}/{}_{}_{}".format(phase,persona_name.lower().lower(),nsites,str(i))
				t_browser_param["profile_tar"]		  = "data/{}/{}_{}_{}".format(phase,persona_name.lower().lower(),nsites,str(i))
				t_browser_param["Persona_Name"]		  = persona_name+".json"
				t_browser_param["Persona_Numb"]       = i
				t_browser_param["Browser_Config"]	  = "config/{}/{}/{}_{}_browser_params_{}.json".format(phase,persona_name,nsites,persona_name,str(i))
				t_browser_param["Manager_Config"]	  = "config/{}/{}/{}_{}_manager_params_{}.json".format(phase,persona_name,nsites,persona_name,str(i))
				t_browser_param["Browser_Config_Def"]	  = "default_browser_params.json"
				t_browser_param["Manager_Config_Def"]	  = "default_manager_params.json"
				t_browser_param["Number_of_Browsers"] = 1
				t_browser_param["Sites"]			  = sites
				t_browser_param["Storage_File"]		  = "storage.js"
				t_browser_param["ublock-origin"]	  = False
				t_browser_param["Ad_Sites"]	 	 	  = ['https://www.accuweather.com']
				t_browser_param["Intent"]	  		  = 'NoIntent'
				t_browser_param["Intent_Sites"]		  = []
				t_browser_param["save_all_content"]	  = False
				t_browser_param["bot_mitigation"]	  = True
				json.dump(t_browser_param, json_file , indent=2)

			with open(os.path.join(temp,'{}_{}_manager_params_{}.json'.format(nsites,persona_name,str(i))),'w') as json_file:
				json.dump(d_manager_param, json_file , indent=2)


			i += 1