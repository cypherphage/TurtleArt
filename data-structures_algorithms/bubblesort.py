def bubblesort(ls):
    for x in range(len(ls)-1,0,-1):
        for i in range(x):
            if ls[i]>ls[i+1]:
                ls[i],ls[i+1]=ls[i+1],ls[i]
    return ls

print(bubblesort([1,34,12,13,23123,23,23,44,4]))
