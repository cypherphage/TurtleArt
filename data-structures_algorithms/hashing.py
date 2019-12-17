def hash(astring,tablesize):
    sum = 0
    counter = 1
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos])*counter
        counter = counter + 1
    return sum % tablesize

print(hash("hello",11))
print(hash("olleh",11))