# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 20:08:05 2026

@author: USER
"""

import random

start, end = 1, 100
count = 10

# 產生亂數
x=random.randint(start, end)    


for i in range(count):
    y=int(input(f"第{i+1}/{count}次：請猜一個數字({start} ~ {end}):"))
    
    if y < start or y > end:
        print("不要亂猜～")
        continue

    if x==y:
        print("恭喜猜對!")
        break
    
    if x>y:
        if y > start:
            start = y + 1
        print("猜大一點")
    else:
        if y < end:
            end = y - 1
        print("猜小一點")
   

if x!=y:
    print("正確答案:%d"%x)



