import urllib.request,time
import re
import socket
import json

url="http://www.sse.com.cn/disclosure/listedinfo/announcement/s_docdatesort_desc.htm";
#url="http://disclosure.szse.cn//disclosure/fulltext/plate/szlatest_24h.js";
def getStockInfo():
    print("----------getStock------------");
    rurl=url;
    response= urllib.request.urlopen(rurl);
    data=response.read().decode('utf-8');
    #print(data);
    p=re.compile(r'href="(.*?)"(.*?)target="_blank">(.*?)<\/a')
    msp=p.findall(data);
    #print(msp);
    for sk in msp:
        #print(sk)
        dealANotice(sk);

def dealANotice(data):
    print(data[2])


getStockInfo();
