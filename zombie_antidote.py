def answer(meetings):
    if (len(meetings) == 1):
        return 1
    else:
        meetings = sorted(meetings, key=getKey)
        sum = 1
        current = meetings[0][1]
        for i in range(1,len(meetings)):
            if (meetings[i][0] >= current):
                sum+=1
                current = meetings[i][1]
        return sum
    
def getKey(item):
    return item[1]
