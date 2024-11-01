def comSum(arr,target):
    result = []
    arr.sort()
    def bt(start,path,current):
        if current == target:
            result.append(path)
            return
        elif current > target:
            return
        for i in range(start,len(arr)):
            if i > start and arr[i] == arr[i - 1]:
                continue
            bt(i+1,path+[arr[i]],current+arr[i])
    bt(0,[],0)
    return result

arr = [10,1,2,7,6,1,5]
target = 8
result = comSum(arr,target)
print(result)