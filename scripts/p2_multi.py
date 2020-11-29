import time
import subprocess
import os
#from threading import Timer

def IntentOrNon(x):

	if(os.path.exists("../data/Phase2/{}_NoIntent".format(x))):
		return "NoIntent"
	else:
		return "Intent"

def getvars(s,i):
	
	varlist        = []
	number         = str(i)
	IntentStatus   = IntentOrNon(s.lower()+'_'+number)
	persona        = s.lower()+'_'+number+'_'+IntentStatus
	containername  = s+number
	configfile     = number+'_'+s+'_browser_params_'+IntentStatus
	mangerfile     = configfile.replace("_browser","_manager")

	varlist.append(persona)
	varlist.append(containername)
	varlist.append(configfile)
	varlist.append(mangerfile)
	varlist.append(IntentStatus)
	return varlist

def process_docker(s,r):
	for i in r:
		
		varlist = getvars(s,i)	
		#print(varlist)

		os.chdir('..')
		cwd = os.getcwd()
		os.chdir('scripts')
		
		
		sudopass = 'cRVuMnmB4S'
		os.system('echo %s | sudo -S docker images' % (sudopass))


		cmd = ['sudo','docker', 'run','-v','{}/config/Phase2/{}/{}.json:/opt/OpenWPM/config/Phase2/{}/{}.json'.format(cwd,s,varlist[3],s,varlist[3]),'-v','{}/config/Phase2/{}/{}.json:/opt/OpenWPM/config/Phase2/{}/{}.json'.format(cwd,s,varlist[2],s,varlist[2]),'-v','{}/flask_data:/opt/OpenWPM/flask_data'.format(cwd),'-v','{}/demo.py:/opt/OpenWPM/demo.py'.format(cwd),'-v', '{}/data/Phase2/{}/:/opt/OpenWPM/data/Phase2/{}'.format(cwd,varlist[0],varlist[0]), '--name', varlist[1], '--shm-size=2g', 'openwpm', 'python', '/opt/OpenWPM/demo.py','config/Phase2/{}/{}.json'.format(s,varlist[2]),'1']
		process  = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

		try:
			oput,err = process.communicate(timeout=5400)
		except:
			cmd = ['sudo','docker','rm','-f',varlist[1]]
			process = subprocess.Popen(cmd)
			oput,err = process.communicate()


		with open('{}/data/Phase2/{}/done.txt'.format(cwd,varlist[0]),'w') as file:
			try:
				file.write(oput.decode("utf-8"))
			except:
				file.write(str(oput))
		with open('{}/data/Phase2/{}/errors.txt'.format(cwd,varlist[0]),'w') as file:
			try:
				file.write(err.decode("utf-8"))
			except:
				file.write(str(err))
		with open('{}/data/Phase2/{}/timestamp.txt'.format(cwd,varlist[0]),'w') as file:
			file.write(str(time.time()))

		sudopass = 'cRVuMnmB4S'
		os.system('echo %s | sudo -S docker images' % (sudopass))
		os.system('sudo docker rm $(sudo docker ps --all -q -f status=exited)')

def collect_ads(s,varlist):

	os.chdir('..')
	cwd = os.getcwd()
	os.chdir('scripts')
	
	sudopass = 'cRVuMnmB4S'
	os.system('echo %s | sudo -S docker images' % (sudopass))

	os.chdir('../data/Phase2/{}'.format(varlist[0]))
	os.system('sudo chmod -R 777 .')
	os.chdir('../../../scripts')

	## Get HB Ads
	cmd = ['sudo','docker', 'run','-v','{}/config/Phase2/{}/{}.json:/opt/OpenWPM/config/Phase2/{}/{}.json'.format(cwd,s,varlist[3],s,varlist[3]),'-v','{}/config/Phase2/{}/{}.json:/opt/OpenWPM/config/Phase2/{}/{}.json'.format(cwd,s,varlist[2],s,varlist[2]),'-v','{}/flask_data:/opt/OpenWPM/flask_data'.format(cwd),'-v','{}/demo.py:/opt/OpenWPM/demo.py'.format(cwd),'-v', '{}/data/Phase2/{}/:/opt/OpenWPM/data/Phase2/{}'.format(cwd,varlist[0],varlist[0]), '--name', varlist[1]+'_2', '--shm-size=2g', 'openwpm', 'python', '/opt/OpenWPM/demo.py','config/Phase2/{}/{}.json'.format(s,varlist[2]),'2']
	process  = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	try:
		oput,err = process.communicate(timeout=5400)
	except:
		cmd = ['sudo','docker','rm','-f',varlist[1]+'_2']
		process = subprocess.Popen(cmd)
		oput,err = process.communicate()

	## Get RTB Ads
	cmd = ['sudo','docker', 'run','-v','{}/config/Phase2/{}/{}.json:/opt/OpenWPM/config/Phase2/{}/{}.json'.format(cwd,s,varlist[3],s,varlist[3]),'-v','{}/config/Phase2/{}/{}.json:/opt/OpenWPM/config/Phase2/{}/{}.json'.format(cwd,s,varlist[2],s,varlist[2]),'-v','{}/flask_data:/opt/OpenWPM/flask_data'.format(cwd),'-v','{}/demo.py:/opt/OpenWPM/demo.py'.format(cwd),'-v', '{}/data/Phase2/{}/:/opt/OpenWPM/data/Phase2/{}'.format(cwd,varlist[0],varlist[0]), '--name', varlist[1]+'_3', '--shm-size=2g', 'openwpm', 'python', '/opt/OpenWPM/demo.py','config/Phase2/{}/{}.json'.format(s,varlist[2]),'3']
	process  = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	try:
		oput1,err1 = process.communicate(timeout=5400)
	except:
		cmd = ['sudo','docker','rm','-f',varlist[1]+'_3']
		process = subprocess.Popen(cmd)
		oput1,err1 = process.communicate()
	
	with open('{}/data/Phase2/{}/ad_collection2_done.txt'.format(cwd,varlist[0]),'w') as file:
		try:
			file.write(oput.decode("utf-8"))
		except:
			file.write(str(oput))
	with open('{}/data/Phase2/{}/ad_collection2_errors.txt'.format(cwd,varlist[0]),'w') as file:
		try:
			file.write(err.decode("utf-8"))
		except:
			file.write(str(err))
	with open('{}/data/Phase2/{}/ad_collection3_done.txt'.format(cwd,varlist[0]),'w') as file:
		try:
			file.write(oput1.decode("utf-8"))
			file.write(str(time.time()))
		except:
			file.write(str(oput1))
	with open('{}/data/Phase2/{}/ad_collection3_errors.txt'.format(cwd,varlist[0]),'w') as file:
		try:
			file.write(err1.decode("utf-8"))
		except:
			file.write(str(err1))

	sudopass = 'cRVuMnmB4S'
	os.system('echo %s | sudo -S docker images' % (sudopass))
	os.system('sudo docker rm $(sudo docker ps --all -q -f status=exited)')

def monitor_ad(s,r):

	for i in r:
		incomplete = True
		varlist = getvars(s,i)
		
		while(incomplete):
			for d in os.listdir(os.path.join("../data/Phase2",varlist[0])):
				if(d == 'timestamp.txt'):
					file = open(os.path.join("../data/Phase2",varlist[0],d),'r')
					ts   = float(file.read())
					file.close()
					cts  = time.time()
					while(cts - ts < 7200):
						time.sleep(10)
						cts = time.time()
					collect_ads(s,varlist)
					incomplete = False
			time.sleep(20)
	return
