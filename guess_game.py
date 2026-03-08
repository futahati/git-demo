# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 20:08:05 2026

@author: USER
"""

import random

# 產生亂數
x=random.randint(1, 100)    
# 提示答案
#print(x)

for i in range(10):
    y=int(input("請猜一個數字(1~100):"))
    
    # 猜對 + break
    if x==y:
        print("恭喜猜對!")
        break
    
    # 猜錯
    if x>y:
        print("猜大一點")
    else:
        print("猜小一點")
   

if x!=y:
    print("正確答案:%d"%x)



