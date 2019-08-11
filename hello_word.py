# coding:utf-8 
'''
created on 2019/8/5

@author:sunyihuan
'''
if __name__ == "__main__":
    print("hello world")
import numpy as np
np.set_printoptions()
Z = np.arange(10, dtype=np.int32)
Z = Z.astype(np.float32, copy=False)