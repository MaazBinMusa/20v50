docker rm $(docker ps -a -q)
rm -r data/Phase1

cd scripts
python setup.py

cd ..
chmod -R 777 .
chmod -R 777 ./

cd scripts
python3 phase1_runner.py
python3 ad_collector.py

cd ..
chmod -R 777 .
chmod -R 777 ./
cd scripts
python final_json_creator.py
