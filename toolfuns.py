import winsound
def notice():
    winsound.PlaySound('ALARM1', winsound.SND_ASYNC);

def adptStr(tstr,data):
    for kk in data:
        tstr=tstr.replace(kk,data[kk]);
    return tstr;
