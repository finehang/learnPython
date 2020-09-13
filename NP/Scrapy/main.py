import requests
import json
from bs4 import BeautifulSoup

def trans(word):
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    from_data = {"i": word,"from": "AUTO","to": "AUTO","smartresult": "dict","client": "fanyideskweb", \
    "salt": "15994523115104","sign": "56adc5f5b83ae99e4223b56e1a47cb77","lts": "1599452311510", \
    "bv": "7b07590bbf1761eedb1ff6dbfac3c1f0","doctype": "json","version": "2.1","keyfrom": "fanyi.web", \
        "action": "FY_BY_CLICKBUTTION"}
    respond = requests.post(url, data=from_data)
    con = json.loads(respond.text)
    return con["translateResult"][0][0]["tgt"]

# print(trans("google"))

url = "https://www.google.com.hk/"

wiki = requests.get(url)

wikisoup = BeautifulSoup(wiki.text, "lxml")
# print(wikisoup)
data = wikisoup.select("#tsf > div:nth-child(2) > div.A8SBwf > div.FPdoLc.tfB0Bf > center > input.RNmpXc")
print(data)
