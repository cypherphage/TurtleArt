from unorderedList import UnorderedList

if __name__ == "__main__":
    ml = UnorderedList()
    ml.add(1)
    ml.add("haha")
    ml.add("wut")
    print(ml)
    print(ml.size())
    #print(ml.pop(3))
    print(ml.end_item())
    print(ml.append("this is the end"))
    print(ml)
    print(ml.append("this is the final end"))
    print(ml)
    ml.insert(12,0)
    print(ml)
    print(ml.insert(12,6))
    print(ml)