import sys,os

path=sys.path[0];
def speak(msg):
    #print(path)
    cmd=path+"\libs\speaker.exe "+msg;
    #print(cmd)
    os.popen(cmd)
