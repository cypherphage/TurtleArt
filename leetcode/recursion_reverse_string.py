def print_rev(string):
    if len(string) == 0:
        return 
    print(string[-1])
    print_rev(string[:-1])
    

print_rev("hello")


def rev_same_list(ls):
    length = len(ls)
    def rev(i):
        if i == length // 2:
            return
        ls[i],ls[-1-i] = ls[-1-i],ls[i]        
        rev(i+1)
    rev(0)
    print(ls)
rev_same_list([1,2,3,4,5,6,7])