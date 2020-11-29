import os
import json
import multiprocessing
from demo import mainfunc

sites = 5

for i in range(1,11,2):
	
	p1  = multiprocessing.Process(target=mainfunc, args=("config/20_50/Adult/{}_Adult_browser_params_{}.json".format(str(sites),str(i)),1))
	p2  = multiprocessing.Process(target=mainfunc, args=("config/20_50/Adult/{}_Adult_browser_params_{}.json".format(str(sites),str(i+1)),1))
	p3  = multiprocessing.Process(target=mainfunc, args=("config/20_50/Control/{}_Control_browser_params_{}.json".format(str(sites),str(i)),1))
	p4  = multiprocessing.Process(target=mainfunc, args=("config/20_50/Control/{}_Control_browser_params_{}.json".format(str(sites),str(i+1)),1))
	p5  = multiprocessing.Process(target=mainfunc, args=("config/20_50/Games/{}_Games_browser_params_{}.json".format(str(sites),str(i)),1))
	p6  = multiprocessing.Process(target=mainfunc, args=("config/20_50/Games/{}_Games_browser_params_{}.json".format(str(sites),str(i+1)),1))
	p7  = multiprocessing.Process(target=mainfunc, args=("config/20_50/Health/{}_Health_browser_params_{}.json".format(str(sites),str(i)),1))
	p8  = multiprocessing.Process(target=mainfunc, args=("config/20_50/Health/{}_Health_browser_params_{}.json".format(str(sites),str(i+1)),1))
	p9  = multiprocessing.Process(target=mainfunc, args=("config/20_50/News/{}_News_browser_params_{}.json".format(str(sites),str(i)),1))
	p10 = multiprocessing.Process(target=mainfunc, args=("config/20_50/News/{}_News_browser_params_{}.json".format(str(sites),str(i+1)),1))
	p11 = multiprocessing.Process(target=mainfunc, args=("config/20_50/Recreation/{}_Recreation_browser_params_{}.json".format(str(sites),str(i)),1))
	p12 = multiprocessing.Process(target=mainfunc, args=("config/20_50/Recreation/{}_Recreation_browser_params_{}.json".format(str(sites),str(i+1)),1))
	p13 = multiprocessing.Process(target=mainfunc, args=("config/20_50/Sports/{}_Sports_browser_params_{}.json".format(str(sites),str(i)),1))
	p14 = multiprocessing.Process(target=mainfunc, args=("config/20_50/Sports/{}_Sports_browser_params_{}.json".format(str(sites),str(i+1)),1))
	
	p1.start() 
	p2.start()
	p3.start() 
	p4.start()
	p5.start() 
	p6.start()
	p7.start() 
	p8.start()
	p9.start() 
	p10.start()
	p11.start() 
	p12.start()
	p13.start() 
	p14.start()

	p1.join() 
	p2.join()
	p3.join() 
	p4.join()
	p5.join() 
	p6.join()
	p7.join() 
	p8.join()
	p9.join() 
	p10.join()
	p11.join() 
	p12.join()
	p13.join() 
	p14.join()
