import os
a=os.popen("ping github.com")
s=a.read()
if "(0% 丢失)" in s:
    print('网络正常')
