def sumOfSub(arr,index,current,result):
    # result = []
    
    if index == len(arr):
        sum = 0
        for i in current:
            sum+= i
        result.append(sum)
        return    
    sumOfSub(arr,index+1,current+[arr[index]],result)
    while index + 1 < len(arr) and arr[index] == arr[index + 1]:
        index += 1
    sumOfSub(arr,index+1,current,result)
    return result
arr = [5,2,1,2]
res = []
result = sumOfSub(arr,0,[],res)
print(result)
