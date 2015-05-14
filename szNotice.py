import urllib.request,time
import re
import socket
import json

##url="http://www.sse.com.cn/disclosure/listedinfo/announcement/s_docdatesort_desc.htm";
url="http://disclosure.szse.cn//disclosure/fulltext/plate/szlatest_24h.js";
def getStockInfo():
    print("----------getStock------------");
    rurl=url;
    response= urllib.request.urlopen(rurl);
    data=response.read().decode('gbk');
    #print(data);
    p=re.compile(r'szzbAffiches=(.*?);')
    msp=p.findall(data);
    ##print(msp);
    objs=msp[0];
    obj=json.loads(objs);
    #print(obj);
    for sk in obj:
        #print(sk)
        dealANotice(sk);

def dealANotice(data):
    print(data[0]+data[2])


getStockInfo();
