import timeit

mysetup = "from math import sqrt"

mycode = '''
def example():
    mylist = []
    for x in range(10000000000000):
        mylist.append(sqrt(x)*sqrt(x+100))
'''

print(timeit.timeit(stmt=mycode,setup=mysetup,number=10000))
