def answer(numbers):
    if (len(numbers) == 2):
        return 2
    else:
        current=0
        index=1
        while(numbers[current]>=0):
            next = numbers[current]
            numbers[current] = (-1 * index)
            index+=1
            current=next
        return (index-(numbers[current]*-1))
    
        
