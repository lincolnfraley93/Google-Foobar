from __future__ import division

def answer(minions):
    list=range(len(minions))
    for i in range(len(minions)):
        list[i]=range(2)
        list[i][0]=(minions[i][0] / (minions[i][1]/minions[i][2]))
        list[i][1]=i
    list=sorted(list, key=lambda element: (element[0],element[1]))
    for i in range(len(list)):
        list[i]=list[i][1]
    return list


