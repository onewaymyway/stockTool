import sys,os



def getPath():
    path=sys.path[0];
    print(path)
    cmd=path+"\speaker.exe 你好";
    os.popen(cmd)


getPath()
