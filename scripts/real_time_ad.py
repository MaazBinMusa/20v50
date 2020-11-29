import sqlite3
import sys
import csv
import pandas as pd
import os
import tldextract
from tqdm import tqdm
from publicsuffix import PublicSuffixList
from parser.BlockListParserr import BlockListParser
from parser.blocklistparser_utils import blocklistparserutils
import time
import json

st = time.time()
psl = PublicSuffixList()
easylist = BlockListParser.BlockListParser('scripts/parser/abpList/easylist.txt')
easyprivacy = BlockListParser.BlockListParser('scripts/parser/abpList/easyprivacy.txt')
bu = blocklistparserutils()


def to_csv(path):
	if(os.path.exists(path+'/2_crawl-data.sqlite') == False):
		return -1
	if(os.path.exists(path+'/tables') == False):
		os.mkdir(path+'/tables')
	
	db = sqlite3.connect(path+'/2_crawl-data.sqlite')
	cursor = db.cursor()
	cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
	tables = cursor.fetchall()
	for table_name in tables:
	    table_name = table_name[0]
	    table = pd.read_sql_query("SELECT * from %s" % table_name, db)
	    table.to_csv(path+'/tables/'+table_name + '.csv', index_label='index', encoding='utf-8')
	cursor.close()
	db.close()
	return 1

def RTBU(path):

	new_path = path
	val = to_csv(new_path)
	if(val == -1):
		return
	df = pd.read_csv(new_path+'/tables/http_responses.csv')
	
	urls = []
	for index,row in df.iterrows():
		start = row['headers'].find('["Content-Type",')
		end = row['headers'].find("]",start)
		if(start == -1):
			continue

		if("image" not in row['headers'][start:end+1]):
			continue
		if easylist.should_block(row['url'], {}):
			urls.append(row['url'])

	urls_tlds = []
	for url in urls:
		res = tldextract.extract(url)
		tld = res.domain
		sub = res.subdomain
		urls_tlds.append((tld,sub,url))
	with open(os.path.join(new_path,'RTB_urls.json'),'w') as file:
		json.dump(urls,file)

	return urls
	
