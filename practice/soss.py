def soss(arr,target):
    result = []
    def bt(start,path,current):
        if current == target:
            result.append(path)
            return 
        if current > target:
            return
        for i in range(start,len(arr)):
            bt(1+i,path+[arr[i]],current+arr[i])
    bt(0,[],0)
    return result

arr = [1,2,3,45,43,2,5]
target = 50
result = soss(arr,target)
print(result)