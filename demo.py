from __future__ import absolute_import
from six.moves import range

from automation import CommandSequence, TaskManager
import sys
import json
import os
import random
from scripts.header_bidding_ad import start
from scripts.header_bidding_ad import cap_images
from scripts.real_time_ad import RTBU
import time
import urllib2

os.chdir('opt/OpenWPM')
config_path  = sys.argv[1] ## Config File Path
mode         = sys.argv[2] ## Flag for Mode ## 1 is ad collection 2 is persona without intent 3 in persona with intent

def callGet(path,mode,**kwargs):
    driver = kwargs['driver']
    js = "var output = [];"\
      "function getCPM()"\
      "{"\
      " var responses = pbjs.getBidResponses();"\
      " Object.keys(responses).forEach(function(adUnitCode){"\
      " var response = responses[adUnitCode];"\
      "     response.bids.forEach(function(bid)"\
      "     {"\
      "         output.push({"\
      "         ad: bid"\
      "         "\
      "         "\
      "         "\
      "         "\
      "         });"\
      "     });"\
      " });"\
      "}"\
      "getCPM();"\
      "return output;"
    status = driver.execute_script(js)
    #save the result in a file
    #print('Ad Content:')
    #print(status)
    path = os.path.join(path,"Header_Bidding"+mode)
    #print(path)
    if(not os.path.exists(path)):
        f = open(path,'w')
        f.close()
    f = open(path,'w')
    stl = [str(i) for i in status]
    st = ' '.join(stl)
    #print(st)
    f.write('\r\n')
    f.write(st)
    f.close()
    return

def real_time_ad(path,mode,**kwargs):
  print("[Running real_time_ad]--------------------------------------")
  start(path)
  print("[Finished real_time_ad]--------------------------------------")
  return

def real_time_img(path,mode,**kwargs):
  print("[Running real_time_img]--------------------------------------")
  cap_images(path,kwargs['driver'])
  print("[Finished real_time_img]--------------------------------------")
  return

def RTB_urls(path):
  print("[Running RTB_urls]--------------------------------------")
  urls = RTBU(path)
  print("[Finished RTB_urls]--------------------------------------")
  return urls

def RTB_imgs(path,file_name,site):
  print("[Running RTB_imgs]--------------------------------------")
  time.sleep(3)
  try:
    print()
    print(site)
    print()
    
    request = urllib2.Request(site,headers={'User-Agent':'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 firefox/2.0.0.11'})
    page = urllib2.urlopen(request)
    
    with open(path+"/{}.png".format(file_name),'wb') as f:
      f.write(page.read())

  except:
    print("[Finished with Error RTB_imgs]--------------------------------------")
    return -1
  
  print("[Finished RTB_imgs]--------------------------------------")
  return 1

if(os.path.exists(config_path)):
    data = open(config_path,'r').read()
    data = json.loads(data)
    persona_path = data['Persona_Path']
    persona_name = data['Persona_Name']
    persona_numb = data['Persona_Numb']
    browser_params_path = data['Browser_Config']
    manager_params_path = data['Manager_Config']
    d_browser_params_path = data['Browser_Config_Def']
    d_manager_params_path = data['Manager_Config_Def']
    NUM_BROWSERS        = data['Number_of_Browsers']
    storage_file        = data['Storage_File']
    sites               = data['Sites']
    Ad_Sites       = data['Ad_Sites']
    Intent_Sites        = data['Intent_Sites']
else:
  print(config_path)
  print("Config File Does Not Exist")
  exit()


if(os.path.exists(persona_path)):
    if (os.path.exists(os.path.join(persona_path,persona_name))):
        print("[Starting Persona Training]-----")
    else:
        print("[Persona Type Does Not Exist] ----- CRITICAL, EXITING")
        #exit()
else:
    print("[Persona Folder Not Available] ----- CRITICAL, EXITING")
    exit()

sites = data['Sites']

# Loads the manager preference and 3 copies of the default browser dictionaries
manager_params, browser_params = TaskManager.load_default_params(browser_params_path,manager_params_path,NUM_BROWSERS)
# Update TaskManager configuration (use this for crawl-wide settings)
# path = persona_path+'/../'+persona_name.replace(".json","").lower()+"_"+str(persona_numb)

path = browser_params[0]['profile_tar']
#path = '.'

# Update browser configuration (use this for per-browser settings)
for i in range(NUM_BROWSERS):
    #print(os.path.join(path,"profile.tar.gz"))
    # Record HTTP Requests and Responses
    browser_params[i]['http_instrument'] = True
    # Enable flash for all three browsers
    browser_params[i]['disable_flash'] = False
    browser_params[i]['headless'] = True  # Launch all browsers headless

    if(not os.path.exists(os.path.join(path,"profile.tar.gz"))):
        browser_params[i]["profile_tar"] = None
        print("set to None")
    browser_params[i]['storage_file']    = storage_file
    #if(str(mode) == '1'):
    #    browser_params[i]['ublock-origin'] = False

os.chdir('../..')
manager_params['data_directory'] = os.path.join(os.path.dirname(os.path.abspath(__file__)),path)
manager_params['log_directory']  = os.path.join(os.path.dirname(os.path.abspath(__file__)),path)
manager_params['database_name'] = str(mode)+'_'+manager_params['database_name']
os.chdir('opt/OpenWPM')

# Instantiates the measurement platform
# Commands time out by default after 60 seconds

if(str(mode) == '1' and sites == [] and Intent_Sites == []):
  exit()

manager = TaskManager.TaskManager(manager_params, browser_params)
# Persona Training Without Intent
# Persona Training Without Intent
#print(browser_params)

if(str(mode) == '1'):

  #  sites = sites[:1]
  for site in sites:
    command_sequence = CommandSequence.CommandSequence(site)
    command_sequence.get(sleep=60, timeout=600)
    command_sequence.dump_profile_cookies(120)
    manager.execute_command_sequence(command_sequence, index='**')

  # Showing Intent if Needed
  # Showing Intent if Needed
  #Intent_Sites = []
  if Intent_Sites != []:
    site = random.choice(Intent_Sites)
    command_sequence = CommandSequence.CommandSequence(site)
    command_sequence.get(sleep=60, timeout=600)
    command_sequence.dump_profile_cookies(120)
    manager.execute_command_sequence(command_sequence, index='**')

# Collecting Ads if Needed
# Collecting Ads if Needed
if(str(mode) == '2'):
  for site in Ad_Sites:
    command_sequence = CommandSequence.CommandSequence(site)
    command_sequence.get(sleep=120, timeout=500)
    path = browser_params[0]['profile_tar']
    if(path == None):
      path = browser_params[0]['profile_archive_dir']

    command_sequence.run_custom_function(callGet,(path,mode,))
    command_sequence.run_custom_function(real_time_ad,(path,mode,),timeout=3000)
    command_sequence.run_custom_function(real_time_img,(path,mode,),timeout=3000)
    command_sequence.dump_profile_cookies(120)
    manager.execute_command_sequence(command_sequence, index='**')
# Shuts down the browsers and waits for the data to finish logging

## Restart the manager for RTB ad extraction
## Restart the manager for RTB ad extraction
if(str(mode) == '3'):
  if(path == None):
    path = browser_params[0]['profile_archive_dir']
  urls = RTB_urls(path)
  success_rtb = {}
  index = 0
  for site in urls:
    persona_path = path.split("/")[-1]
    file_name = persona_path+"_RTB_image_{}".format(str(index))
    ans = RTB_imgs(path,file_name,site)
    index = index + 1

    if(ans == 1):
      success_rtb[file_name] = site

  with open(os.path.join(path,'RTB_urls.json'),'w') as file:
    json.dump(success_rtb,file)

manager.close()

