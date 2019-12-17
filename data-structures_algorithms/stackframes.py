from pythonds.basic import Stack

s = Stack()
def tostr(num,base):
    strconv = "0123456789ABCDEF"
    while num > 0:
        if num < base:
            s.push(strconv[num])
        else:
            s.push(strconv[num%base])
        num = num // base
    out = ""
    while  not s.isEmpty():
        out = out + str(s.pop())

    return out



print(tostr(999999,2))