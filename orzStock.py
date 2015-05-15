import urllib.request,time
import re
import socket
import json
import winsound

from toolfuns import *

from myStock import Stocks


socket.setdefaulttimeout(8.0)

url="http://bdcjhq.hexun.com/quote?s2=";


sps={
    "na":"名称",
    "pc":"昨收盘",
    "op":"今开盘",
    "vo":"成交量",
    "tu":"成交额",
    "hi":"最高价",
    "lo":"最低价",
    "la":"现价",
    "type":"类型",
    "time":"时间",
    "sy":"市盈率",
    "lt":"流通股数",
    "sz":"总市值",
    "hs":"换手率",
    "is":"unknow",
    "bp1":"停牌",
    "zf":"涨幅"
    };
diss={
    ##"na":"名称",
    ##"pc":"昨收盘",
    #"op":"今开盘",
    #"vo":"成交量",
    #"tu":"成交额",
    "hi":"最高价",
    "lo":"最低价",
    "la":"现价",
    ##"time":"时间",
    ##"sy":"市盈率",
    ##"lt":"流通股数",
    ##"sz":"总市值",
    "hs":"换手率",
    "zf":"涨幅",
    "num":"代码"
    };

#rules={}

tmpl="**na:la(zf%)(lo:hi)*num*";
tmplNotice="!!!!!!!!!na:la(zf%)(lo:hi)*num*!!!!!!!";
#dRule='float(data["zf"])<9.95';
rurl="";
def getStockInfo():
    print("----------getStock------------");
    
    #print(rurl);
    response= urllib.request.urlopen(rurl);
    data=response.read().decode('gbk');
    ##print(data);
    p=re.compile(r'bdcallback\((.*?)\)')
    msp=p.findall(data);
    ##print(msp);
    objs=msp[0];
    objs=objs.replace(".sz",".深圳");
    objs=adptJSon(objs);
    ##print(objs);
    obj=json.loads(objs);
    ##print(obj);
    for stock in obj:
        tstock=obj[stock];
        if "la" in tstock:
            if float(tstock["pc"])<=0:
                continue;
            percent=100*(float(tstock["la"])-float(tstock["pc"]))/float(tstock["pc"]);
            tstock["num"]=stock.split(".")[0];
            tstock["zf"]="%.2f"%percent;
            printAStock(tstock,stock);
        
        
    ##print(data);
    

def adptJSon(data):
    
    for kk in sps:
        data=data.replace(kk,'"'+kk+'"');
    return data;


def printAStock(data,num):
    ##print(data);
    hookStock(data);
    print(adptStr(tmpl,data));
    return
    global sps
    disarr=[]
    for key in data:
        if key in diss:
            disarr.append(diss[key]+":"+data[key]);
            ##print(sps[key]+":"+data[key]);

    print(",".join(disarr))

def hookStock(data):
    #print(eval('float(data["zf"])<9.95'));
    code=data["num"];
    if code in mStock.rules:
        if eval(mStock.rules[code]):
            notice();
            print(adptStr(tmplNotice,data));
    return
    if float(data["zf"])<9.95 :
        notice();
        print(adptStr(tmplNotice,data));
        
    pass





    
def mainLoop():



    #getStockInfo();
    while(1):
        try:
            getStockInfo();
            time.sleep(5);
        except Exception as e:
            print(e);
            time.sleep(5);
        
        
mStock=Stocks();
rurl=url+",".join(mStock.stocksA);
mainLoop();
