import time
import subprocess
import os
#from threading import Timer


def process_docker(s,r):
	for i in r:
		
		persona = s+'_'+str(i)
		directory_name = s.split('_')[0]
		typpe = s.split('_')[0]
		number = str(i)
		persona = s.split('_')[0].lower()+'_'+s.split('_')[-1]+'_'+number
		container_name = s+number

		config_file = s.split('_')[-1]+'_'+typpe

		os.chdir('..')
		cwd = os.getcwd()
		os.chdir('scripts')

		#print(directory_name,persona,number,container_name,config_file,cwd)
		#exit()

		#Some other thread is already running this
		if(os.path.exists('{}/data/Phase1/{}/openwpm.log'.format(cwd,persona)) or os.path.exists('{}/data/Phase1/{}/done.txt')):
			continue
		
		#print(number,typpe,config_file)
		#break
		#os.system('sudo docker run -v {}/demo.py:/opt/OpenWPM/demo.py -v {}/data/Phase1/{}/:/opt/OpenWPM/data/Phase1/{} --name {} --shm-size=2g -d openwpm python /opt/OpenWPM/demo.py Config/Phase1/{}/{}_browser_params_{}.json 2'.format(cwd,cwd,persona,persona,persona,typpe,config_file,number))
		
		#print('Hey')
		sudopass = 'cRVuMnmB4S'
		os.system('echo %s | sudo -S docker images' % (sudopass))
		#print('Hey')
		#continue

		cmd = ['sudo','docker', 'run','-v','{}/flask_data:/opt/OpenWPM/flask_data'.format(cwd),'-v','{}/demo.py:/opt/OpenWPM/demo.py'.format(cwd),'-v', '{}/data/Phase1/{}/:/opt/OpenWPM/data/Phase1/{}'.format(cwd,persona,persona), '--name', container_name, '--shm-size=2g', 'openwpm', 'python', '/opt/OpenWPM/demo.py','config/Phase1/{}/{}_browser_params_{}.json'.format(directory_name,config_file,number),'1']
		process  = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		#timer = Timer(30, process.kill)
		try:
			oput,err = process.communicate(timeout=5400)
		except:
			cmd = ['sudo','docker','rm','-f',container_name]
			process = subprocess.Popen(cmd)
			oput,err = process.communicate()
		time.sleep(7)

		## Write done.txt

		with open('{}/data/Phase1/{}/done.txt'.format(cwd,persona),'w') as file:
			try:
				file.write(oput.decode("utf-8"))
			except:
				file.write(str(oput))
		with open('{}/data/Phase1/{}/errors.txt'.format(cwd,persona),'w') as file:
			try:
				file.write(err.decode("utf-8"))
			except:
				file.write(str(err))

		#print("Yea this waits"*10)


def collect_ads(s,r):
	for i in r:
		
		persona = s+'_'+str(i)
		directory_name = s.split('_')[0]
		typpe = s.split('_')[0]
		number = str(i)
		persona = s.split('_')[0].lower()+'_'+s.split('_')[-1]+'_'+number
		container_name = s+number

		config_file = s.split('_')[-1]+'_'+typpe

		os.chdir('..')
		cwd = os.getcwd()
		os.chdir('scripts')
		
		#print(number,typpe,config_file)
		#break
		#os.system('sudo docker run -v {}/demo.py:/opt/OpenWPM/demo.py -v {}/data/Phase1/{}/:/opt/OpenWPM/data/Phase1/{} --name {} --shm-size=2g -d openwpm python /opt/OpenWPM/demo.py Config/Phase1/{}/{}_browser_params_{}.json 2'.format(cwd,cwd,persona,persona,persona,typpe,config_file,number))
		
		#print('Hey')
		sudopass = 'cRVuMnmB4S'
		os.system('echo %s | sudo -S docker images' % (sudopass))
		#print('Hey')
		#continue

		## Get HB Ads
		cmd = ['sudo','docker', 'run','-v','{}/flask_data:/opt/OpenWPM/flask_data'.format(cwd),'-v','{}/demo.py:/opt/OpenWPM/demo.py'.format(cwd),'-v', '{}/data/Phase1/{}/:/opt/OpenWPM/data/Phase1/{}'.format(cwd,persona,persona), '--name', container_name+'_2', '--shm-size=2g', 'openwpm', 'python', '/opt/OpenWPM/demo.py','config/Phase1/{}/{}_browser_params_{}.json'.format(directory_name,config_file,number),'2']
		process  = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		try:
			oput,err = process.communicate(timeout=5400)
		except:
			cmd = ['sudo','docker','rm','-f',container_name+'_2']
			process = subprocess.Popen(cmd)
			oput,err = process.communicate()

		## Get RTB Ads
		cmd = ['sudo','docker', 'run','-v','{}/flask_data:/opt/OpenWPM/flask_data'.format(cwd),'-v','{}/demo.py:/opt/OpenWPM/demo.py'.format(cwd),'-v', '{}/data/Phase1/{}/:/opt/OpenWPM/data/Phase1/{}'.format(cwd,persona,persona), '--name', container_name+'_3', '--shm-size=2g', 'openwpm', 'python', '/opt/OpenWPM/demo.py','config/Phase1/{}/{}_browser_params_{}.json'.format(directory_name,config_file,number),'3']
		process  = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		try:
			oput1,err1 = process.communicate(timeout=5400)
		except:
			cmd = ['sudo','docker','rm','-f',container_name+'_3']
			process = subprocess.Popen(cmd)
			oput1,err1 = process.communicate()
		time.sleep(7)
		## Write done.txt

		with open('{}/data/Phase1/{}/ad_collection2_done.txt'.format(cwd,persona),'w') as file:
			try:
				file.write(oput.decode("utf-8"))
			except:
				file.write(str(oput))
		with open('{}/data/Phase1/{}/ad_collection2_errors.txt'.format(cwd,persona),'w') as file:
			try:
				file.write(err.decode("utf-8"))
			except:
				file.write(str(err))
		with open('{}/data/Phase1/{}/ad_collection3_done.txt'.format(cwd,persona),'w') as file:
			try:
				file.write(oput1.decode("utf-8"))
			except:
				file.write(str(oput1))
		with open('{}/data/Phase1/{}/ad_collection3_errors.txt'.format(cwd,persona),'w') as file:
			try:
				file.write(err1.decode("utf-8"))
			except:
				file.write(str(err1))

		#print("Yea this waits"*10)
