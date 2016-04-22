import math

def answer(x):
    i=0
    list=[]
    while(x!=0):
        position=(x/math.pow(3,i))%3
        if (position==0):
            list.append("-")
        elif (position==1):
            x=x-math.pow(3,i)
            list.append("R")
        else:
            x=x+math.pow(3,i)
            list.append("L")
        i+=1
    return list
