def LargestPair(num):
    num1 = str(num)
    list1 = []
    list2 = []
    for i in range(0,len(num1)-1):
        s = int(num1[i])+int(num1[i+1])
        list1.append(s)
    return list1

print(LargestPair(363346))