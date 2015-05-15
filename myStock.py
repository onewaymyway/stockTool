

dRule='float(data["zf"])>10 or float(data["zf"])<-9';
def getStockList(fileName):
    rules={};
    stocks=[];
    f=open(fileName,"r",encoding="utf-8");
    data=f.readlines();
    f.close();
    for line in data:
        line=line.strip();
        cr=line.split(",");
        code=cr[0];
        if len(cr)>1:
            trule=cr[1];
        else:
            trule=dRule;
        rules[code]=trule;
        stocks.append(code);
    rst={};
    rst["stocks"]=stocks;
    rst["rules"]=rules;
    return rst;

codeType={
    "6":"sh",
    "0":"sz",
    "3":"sz"
    }
def adptStockCode(code):
    return code+"."+codeType[code[0]];

def getStocks(stockList):
    rst=[];
    for stock in stockList:
        rst.append(adptStockCode(stock));
    return rst;

class Stocks:

    def __init__(self,file="stockList.txt"):

        data=getStockList(file);
        self.stocks=data["stocks"];
        self.rules=data["rules"];
        self.stocksA=getStocks(self.stocks);

