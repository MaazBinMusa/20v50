from publicsuffix import PublicSuffixList
from BlockListParserr import BlockListParser
from blocklistparser_utils import blocklistparserutils
import time
import json

st = time.time()
psl = PublicSuffixList()
easylist = BlockListParser.BlockListParser('abpList/easylist.txt')

bu = blocklistparserutils()
# Sample data

tp_reqs = {}
n=0
with open('third_party_requests.json') as f: 
    tp_reqs = json.load(f)
for domain in tp_reqs: 
    for request in tp_reqs[domain]:
        url =request['request_url']
        options = request['block_options']
        if easylist.should_block(url, options):
            print("URL {} would have been blocked by easylist").format(url)
            exit()
        n+=1
print('Took {}s'.format(time.time() - st))