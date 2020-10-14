##
# 姓名:王昱翔
# 座位號碼:07
# 修改檔名到你的座位號碼
##

import os
import sys

print('我是{},座位號碼是{}'.format("王昱翔", '07'))
# e.g. C:\Python\Python38\python.exe
print("我使用的python的路徑是:{}".format(sys.executable))
print("我的工作目錄是:%s" % os.getcwd())
print("我執行的這個檔案名稱是:{}".format(sys.argv[0]))
print(f'我的環境會找的路徑有:{sys.path}')
