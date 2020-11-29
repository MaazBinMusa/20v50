from p2_multi import process_docker
from p2_multi import monitor_ad
import multiprocessing
import os
from os import system


sets = []

for d in os.listdir('../data/personas/'):
	part = d.split('.json')[0]
	if part not in sets:
		sets.append(part)


for s in sets:

    p1 = multiprocessing.Process(target=process_docker, args=(s,range(1,128))) 
    p2 = multiprocessing.Process(target=process_docker, args=(s,range(128,256)))
    p3 = multiprocessing.Process(target=process_docker, args=(s,range(256,384)))
    p4 = multiprocessing.Process(target=process_docker, args=(s,range(384,512)))
    p5 = multiprocessing.Process(target=process_docker, args=(s,range(512,640)))
    p6 = multiprocessing.Process(target=process_docker, args=(s,range(640,768)))
    p7 = multiprocessing.Process(target=process_docker, args=(s,range(768,896)))
    p8 = multiprocessing.Process(target=process_docker, args=(s,range(896,1025)))
    p1.start() 
    p2.start()
    p3.start() 
    p4.start()
    p5.start() 
    p6.start()
    p7.start() 
    p8.start()

    b1 = multiprocessing.Process(target=monitor_ad, args=(s,range(1,128))) 
    b2 = multiprocessing.Process(target=monitor_ad, args=(s,range(128,256)))
    b3 = multiprocessing.Process(target=monitor_ad, args=(s,range(256,384)))
    b4 = multiprocessing.Process(target=monitor_ad, args=(s,range(384,512)))
    b5 = multiprocessing.Process(target=monitor_ad, args=(s,range(512,640)))
    b6 = multiprocessing.Process(target=monitor_ad, args=(s,range(640,768)))
    b7 = multiprocessing.Process(target=monitor_ad, args=(s,range(768,896)))
    b8 = multiprocessing.Process(target=monitor_ad, args=(s,range(896,1025)))
    b1.start() 
    b2.start()
    b3.start() 
    b4.start()
    b5.start() 
    b6.start()
    b7.start() 
    b8.start()
