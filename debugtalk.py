import os  
							
import sys
							
root_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #获取当前工作路径、保存路径、获取当前路径的几种方法
							
sys.path.append(root_path)  #把获取到的工作路径添加到 系统路径下 。
import time

import os


def ENV(keyname):
    values = os.environ.get(keyname,"")
    return values

def sleep(n_secs):
    time.sleep(n_secs)