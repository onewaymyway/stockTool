import urllib.request,time
import re
import socket
import json
from toolfuns import *
from myStock import Stocks

noticeAll={}
def getSZNotice():
    #print("----------getStock------------");
    url="http://disclosure.szse.cn//disclosure/fulltext/plate/szlatest_24h.js";
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
    rsts=[];
    for sk in obj:
        #print(sk)
        tNotice=dealASZNotice(sk);
        rsts.append(tNotice);
    return rsts;

def dealASZNotice(data):
    rst={};
    rst["code"]=data[0];
    rst["title"]=data[2];
    rst["url"]="http://disclosure.szse.cn/"+data[1];
    dealNoticeCM(rst);
    return rst;

def getSHNotice():
    #print("----------getStock------------");
    url="http://www.sse.com.cn/disclosure/listedinfo/announcement/s_docdatesort_desc.htm";
    rurl=url;
    response= urllib.request.urlopen(rurl);
    data=response.read().decode('utf-8');
    #print(data);
    p=re.compile(r'href="(.*?)"(.*?)target="_blank">(.*?)<\/a')
    msp=p.findall(data);
    #print(msp);
    rsts=[];
    for sk in msp:
        #print(sk)
        tNotice=dealASHNotice(sk);
        rsts.append(tNotice);
    return rsts;

def dealASHNotice(data):
    #print(data[2])
    rrs=data[2].split(":");
    rst={};
    rst["code"]=rrs[0].strip();
    rst["title"]=rrs[1].strip();
    rst["url"]=data[0];
    dealNoticeCM(rst);
    return rst;
    
def dealNoticeCM(data):
    noticeAll[data["code"]]=data;
    pass;


def checkNotice():
    noticeAll={};
    notices=getSZNotice()+getSHNotice();
    #print(notices);
    for tstock in notices:
        code=tstock["code"];
        if code in mStock.rules:
            
            nUrl=tstock["url"];
            if nUrl in rNotice:
                pass;
            else:
                print(adptStr(wNotice,tstock))
                notice();
            rNotice[nUrl]=tstock;
            

rNotice={}
wNotice="---code----\n title \n url";
mStock=Stocks();

def mainLoop():


    while(1):
        try:
            checkNotice();
            time.sleep(5);
        except Exception as e:
            print(e);
            time.sleep(5);

if __name__ == '__main__':
    mainLoop()
