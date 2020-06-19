import os
import time
while True:
    a = os.popen("ping 192.168.0.122")
    s = a.read()
    time2 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(time2)
    if "(0% 丢失)" in s:
        with open(r'C:\Users\Administrator\Desktop\ip_jiankong.txt', "a") as f:
            time.sleep(1)
            f.write(time2 + " :  网络正常"+'\n')
    elif "(100% 丢失)" in s:
        with open(r'C:\Users\Administrator\Desktop\ip_jiankong.txt', "a") as f:
            time.sleep(1)
            f.write(time2 + " :  网络异常"+'\n')

