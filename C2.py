# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 16:21:56 2024

@author: loboh
"""
import numpy as np
import matplotlib.pyplot as plt

plt.figure(dpi=720)
e=1e-14

#for mathematical context:
   
#alpha (a) - number being square rooted.
#k - difference in the guess versus a.

# bisection- x'^2 - a = k
#newt_raph- x_n+1 = x_n - ( f(x_n) / f'(x_n) )


#the purpose of this code is to use numerical methods in order to
#find a (good enough) estimate / accurate value for the square root
#of a given number. this code will be using bisection and newton raphson
#in order to converge on a solution with different efficiencies.

#the code will also provide a difference in iterations
#in order to show the efficiency while also visually illustrating
#the percentage differences between the "current iteration"
#vs the actual value of the square root.

a_input = float(input("number being sqr_rootd: "))


def bisection(a,i_max): #a - number being sqrt'ed
    bisect_list=[]
    x_low = 0               #i_max - max_iterations
    x_high = 0    #<preamble
    k=0       #due to nature of bisection, no variables->
    x_mid=0
    i=0
    lastguess = x_mid+3
          #can be established from the start.
    if a > 1:
        x_high = a  
    elif a == 1 or a == 0:
        return a,[[0,a]]
    else:
        x_high = 1   #if x_high is not 1, bisection will diverge below for a < 1.
    while x_mid**2 != a and x_mid != lastguess:   #runtime condition
        lastguess = x_mid
        x_mid = ((x_high+x_low)/2)
        k = x_mid**2 - a #finding k with bisection              
        if k < 0:           #to determine whether the guess is higher
            x_low = x_mid   #or lower than the true value.
        else:
            x_high = x_mid
        bisect_list.append([i,x_mid])
        i+=1
    return x_mid,bisect_list

def newt_raph(a,i_nput): #same inputs as bisection.
    newt_list=[[0,a]]
    x_n = a     #declaring new x
    x_0 = 0 #declaring initial guess
    i=0
    if x_n == 0 or x_n == 1:
        return a,[[0,a]]
    while x_n**2 != a and x_n != x_0:
        x_0 = x_n      #setting x_n to be x_n+1    #f(x) = x^2 - a.
        x_n = x_0 - ((x_0**2-a)/(2*x_0))       #newton raphson given that
        if np.abs(x_0-x_n) < e:
            break
        newt_list.append([i+1,x_n]) #newt_list already begins with 0
        i+=1
#        print(x_n)
    return x_n,newt_list         #for next iteration

result_bisec,list_1=bisection(a_input,100)
result_newt,list_2=newt_raph(a_input,10)
list_bisect = np.array(list_1)
list_newt = np.array(list_2)
print("{} bisection".format(result_bisec))
print("{} newton raphson".format(result_newt))
print("{} numpy (for reference)".format(np.sqrt(a_input)))

plt.semilogy(list_bisect[:,0],np.abs((100*(((list_bisect[:,1])-np.sqrt(a_input)))/np.sqrt(a_input))),label="Bisection")
plt.semilogy(list_newt[:,0],np.abs((100*(((list_newt[:,1])-np.sqrt(a_input)))/np.sqrt(a_input))),label="Newton Raphson")
plt.xlabel("Iterations")
plt.ylabel("Absolute Percent Difference")
plt.legend()

#a for assignment - 303.617.