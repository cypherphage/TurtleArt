def selectionsort(ls):
    for x in range(len(ls)-1,0,-1):
        pos = 0
        for i in range(1,x+1):
            if ls[i] > ls[pos]:
                pos = i
        ls[pos],ls[i]=ls[i],ls[pos]
    return ls

print(selectionsort([23,4,5,2,4,6,89,-1,0,-1]))
            
        

            
