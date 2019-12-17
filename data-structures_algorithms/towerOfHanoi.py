def hanoi(n,f,h,t):
    if n==0:
        pass
    else:
        hanoi(n-1,f,t,h)
        move(f,t)
        hanoi(n-1,h,f,t)

def move(f,t):
    print("Moving disk from ", f , " to " , t)

hanoi(3,"A","B","C")