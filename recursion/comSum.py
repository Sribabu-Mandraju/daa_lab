def comSum(arr, target):
    result = []
    def bt(start, path, current):
        if current == target:
            result.append(path)
            return
        if current > target:
            return
        for i in range(start, len(arr)):
            bt(i, path + [arr[i]], current + arr[i])  
    bt(0, [], 0)
    return result

arr = [1, 2, 3, 45, 43, 2, 5]
target = 10
result = comSum(arr, target)
print(result)
