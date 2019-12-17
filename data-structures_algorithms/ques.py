def listsum(ls):
    if len(ls) == 1:
        return ls[0]
    else:
        return ls[0] + listsum(ls[1:])

print(listsum([1,2,3,4,5]))

def tostr(num,base):
    strconv = "0123456789ABCDEF"
    if num < base:
        return strconv[num]
    else:
        return tostr(num//base,base) + strconv[num%base]

print(tostr(999999,16))

def rev(instr):
    if len(instr) == 1:
        return instr[-1]
    else:
        return instr[-1] + rev(instr[:-1])
print(rev("hello"))

def ispal(instr):
    instr = instr.replace(" ","").replace(",","").replace("-","").lower()
    isPal = True
    if instr[0] != instr[-1]:
        return False

    if len(instr) == 1 or 0:
        return isPal 
    else:
        return ispal(instr[1:-1])

print(ispal("Reviled did I live, said I, as evil I did deliver"))