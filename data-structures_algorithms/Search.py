def seqSearch(ls,x):
    pos = 0
    found = False
    while pos < len(ls) and not found:
        if ls[pos] == x:
            found = True
        pos = pos + 1
    return found

print(seqSearch([11,3,45,23,4,5,2],22))

def binarySearch(ls,x):
    first = 0 
    last = len(ls) - 1
    found = False
    while first <= last and not found:
        mid = (first + last) // 2
        if ls[mid] == x:
            found = True
        else:
            if ls[mid] < x:
                first = mid + 1
            else:
                last = mid - 1
    return found

print(binarySearch([1,2,3,4,6,8,9],0))

y = []

def binaryRecSearch(ls,x):
    if len(ls) == 0:
        return False
    else:
        mid = len(ls)//2
        y.append(ls[mid])
        if ls[mid] == x:
            return True
        else:
            if ls[mid] > x:
                return binaryRecSearch(ls[:mid],x)
            else:
                return binaryRecSearch(ls[mid+1:],x)

print(binaryRecSearch([3, 5, 6, 8, 11, 12, 14, 15, 17, 18],16))
print(y)

