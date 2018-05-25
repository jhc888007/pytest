#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np  
import matplotlib.pyplot as plt  
from scipy import optimize  
  
#直线方程函数  
def f_1(x, A, B):  
    return A*x + B  
  
#二次曲线方程  
def f_2(x, A, B, C):  
    return A*x*x + B*x + C  
  
#三次曲线方程  
def f_3(x, A, B, C, D):  
    return A*x*x*x + B*x*x + C*x + D  
  
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
print "BEGIN"
with open("temp2.txt") as input:
    for line in input:
        v = line.strip().split('\t')
        if len(v) != 2:
            continue
        num = int(v[0])
        score = float(v[1])
        if score > 100.0 or num > 200:
            continue
        x.append(num)
        y.append(score)
        if num > x_max:
            x_max = num

print y_max
print z_max
    
#plot_test(x, y, x_max)
plt.figure()    
  
#绘制散点  
plt.scatter(x[:], y[:], 25, "red")
plt.show()
        