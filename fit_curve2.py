#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np 
import random 
import matplotlib.pyplot as plt  
from scipy import optimize  
import math
  
#直线方程函数  
def f_1(x, A, B):  
    return A*x + B  
  
#二次曲线方程  
def f_2(x, A, B, C):  
    return A*x*x + B*x + C  
  
#三次曲线方程  
def f_3(x, A, B, C, D):  
    return A*x*x*x + B*x*x + C*x + D  
    
#四次曲线方程  
def f_4(x, A, B, C, D, E):  
    return A*x*x*x*x + B*x*x*x + C*x*x + D*x + E 

def fit_3(x0, y0, max_x):
    A, B, C, D= optimize.curve_fit(f_3, x0, y0)[0]  
    x = np.arange(0, max_x, max_x/100)  
    y = A*x*x*x + B*x*x + C*x + D
    return x, y

def fit_4(x0, y0, max_x):
    A, B, C, D, E = optimize.curve_fit(f_4, x0, y0)[0]  
    x = np.arange(0, max_x, max_x/100)  
    y = A*x*x*x*x + B*x*x*x + C*x*x + D*x + E 
    return x, y

def plot_test(x0, y0, max_x):  
    print "TO PLOT"  
    plt.figure()    
  
    #绘制散点  
    plt.scatter(x0[:], y0[:], 25, "red")  
  
    #直线拟合与绘制
    print "TO FIT1" 
    A1, B1 = optimize.curve_fit(f_1, x0, y0)[0]  
    x1 = np.arange(0, max_x, max_x/100)  
    y1 = A1*x1 + B1  
    plt.plot(x1, y1, "blue")  
  
    #二次曲线拟合与绘制
    print "TO FIT2" 
    A2, B2, C2 = optimize.curve_fit(f_2, x0, y0)[0]  
    x2 = np.arange(0, max_x, max_x/100)  
    y2 = A2*x2*x2 + B2*x2 + C2   
    plt.plot(x2, y2, "green")  
  
    #三次曲线拟合与绘制
    print "TO FIT3" 
    A3, B3, C3, D3= optimize.curve_fit(f_3, x0, y0)[0]  
    x3 = np.arange(0, max_x, max_x/100)  
    y3 = A3*x3*x3*x3 + B3*x3*x3 + C3*x3 + D3   
    plt.plot(x3, y3, "purple")  
  
    plt.title("test")  
    plt.xlabel('x')  
    plt.ylabel('y')  
  
    plt.show()  
  
    return 
    
x = []
x_max = 0
y = []
y_max = 0
z = []
z_max = 0
t = []
print "BEGIN"
with open("temp2.txt") as input:
    for line in input:
        v = line.strip().split('\t')
        if len(v) != 6:
            continue
        num = int(v[1])
        playcnt = int(v[2])
        lovecnt = int(v[3])
        showcnt = int(v[4])
        if num >= 200:
            continue
        if playcnt > 10000000 or lovecnt > 30000:
            continue
        if showcnt == 0:
            continue
        x.append(num)
        y.append(playcnt)
        z.append(lovecnt)
        t.append(showcnt)
        if num > x_max:
            x_max = num
        if playcnt > y_max:
            y_max = playcnt
        if lovecnt > z_max:
            z_max = lovecnt
    
print y_max
print z_max

#随机分段取值
SEG_SEP = 50
SEG_NUM = 100
inidx = range(len(x))
random.shuffle(inidx)
hashdic = {}
outidx = []
for i in inidx:
    hash = x[i]/SEG_SEP
    if hash not in hashdic:
        hashdic[hash] = 1
    elif hashdic[hash] >= SEG_NUM:
        continue
    else:
        hashdic[hash] += 1
    outidx.append(i)
x1 = []
y1 = []
z1 = []
print len(hashdic)*SEG_NUM
print len(outidx)

for i in outidx:
    x1.append(x[i])
    y1.append(math.log(y[i]*100000/y_max/t[i]+1))
    z1.append(math.log(z[i]*100000/z_max/t[i]+1))
    #y1.append(math.log(float(y[i])+1))
    #z1.append(math.log(float(z[i])+1))

    
plt.figure()    
  
#绘制散点  
plt.scatter(x1[:], y1[:], 1, "red")
plt.scatter(x1[:], z1[:], 1, "blue")

#拟合
x3, y3 = fit_4(x1, y1, x_max)
plt.plot(x3, y3, "purple")
x3, z3 = fit_4(x1, z1, x_max)
plt.plot(x3, z3, "yellow")    
    
#展示图片
plt.show()
        