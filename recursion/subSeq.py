def genSub(arr,index,current):
    if index == len(arr):
        print(current)
        return
    genSub(arr,index+1,current+[arr[index]])
    while index + 1 < len(arr) and arr[index] == arr[index + 1]:
        index += 1
    genSub(arr,index+1,current)
    
arr = [1,2,2]
arr.sort()
genSub(arr,0,[])