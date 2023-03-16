def TwoSum(arr):
    index = 0
    list1 = []
    list2 = []
    for index in range(1,len(arr)):
        for i in arr[1:-1]:
            s = arr[arr.index(i)]+arr[index]
            if s == arr[0]:
                a = arr[arr.index(i)]
                b = arr[index]
                list1.append(a)
                list2.append(b)
        index +=1
    return list1,list2