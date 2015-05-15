#stockTools

股票相关的小工具

stockList.txt 要监控的股票列表
格式：
每行：股票代码,报警条件
实例
603227,float(data["zf"])<9.95
600701
600293,float(data["zf"])<9.95 and 1==1

可供调用参数：
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

orzStock.py 监控股票现价
orzNotice.py 监控是否有新公告