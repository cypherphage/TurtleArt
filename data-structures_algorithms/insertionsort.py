def insertionsort(ls):
    for index in range(1,len(ls)):
        currentvalue = ls[index]
        pos = index

        while pos > 0 and ls[pos-1] > currentvalue:
            ls[pos] = ls[pos-1]
            pos = pos - 1
        
        ls[pos] = currentvalue
        
        
