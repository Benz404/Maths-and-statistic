"""
Created on Sat Sep 19 10:22:35 2020

@author: the_benz
"""
while True:
    import math
    print("please enter starting limit")
    start=int(input())
    print("please enter ending limit")
    end=int(input())
    def expo_values(start,end):
        x=start
        list_of_values=[]
        while(x<=end):
            exponential_values=math.exp(x)
            list_of_values.append(exponential_values)
            x=x+1
        print (list_of_values)
    expo_values(2, end)