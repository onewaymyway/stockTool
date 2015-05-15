import winsound
import os
def speak(msg):
    cmd="speaker.exe "+msg;
    os.popen(cmd)
    
def notice(msg="警告"):
    #winsound.PlaySound('ALARM1', winsound.SND_ASYNC);
    speak(msg)

def adptStr(tstr,data):
    for kk in data:
        tstr=tstr.replace(kk,data[kk]);
    return tstr;


if __name__ == '__main__':
    notice();
