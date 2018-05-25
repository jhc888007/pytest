#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np  
import matplotlib.pyplot as plt  
from scipy import optimize  
  
#ֱ�߷��̺���  
def f_1(x, A, B):  
    return A*x + B  
  
#�������߷���  
def f_2(x, A, B, C):  
    return A*x*x + B*x + C  
  
#�������߷���  
def f_3(x, A, B, C, D):  
    return A*x*x*x + B*x*x + C*x + D  
  
def plot_test():  
  
    plt.figure()  
  
    #��ϵ�  
    x0 = [1, 2, 3, 4, 5]  
    y0 = [1, 3, 8, 18, 36]  
  
    #����ɢ��  
    plt.scatter(x0[:], y0[:], 25, "red")  
  
    #ֱ����������  
    A1, B1 = optimize.curve_fit(f_1, x0, y0)[0]  
    x1 = np.arange(0, 6, 0.01)  
    y1 = A1*x1 + B1  
    plt.plot(x1, y1, "blue")  
  
    #����������������  
    A2, B2, C2 = optimize.curve_fit(f_2, x0, y0)[0]  
    x2 = np.arange(0, 6, 0.01)  
    y2 = A2*x2*x2 + B2*x2 + C2   
    plt.plot(x2, y2, "green")  
  
    #����������������  
    A3, B3, C3, D3= optimize.curve_fit(f_3, x0, y0)[0]  
    x3 = np.arange(0, 6, 0.01)  
    y3 = A3*x3*x3*x3 + B3*x3*x3 + C3*x3 + D3   
    plt.plot(x3, y3, "purple")  
  
    plt.title("test")  
    plt.xlabel('x')  
    plt.ylabel('y')  
  
    plt.show()  
  
    return 
    
plot_test() 