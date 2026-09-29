def majorityElement(arr):
    
    candidate = None
    count = 0
    
    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
            
   
    actual_count = 0
    for num in arr:
        if num == candidate:
            actual_count += 1
            
   
    if actual_count > len(arr) // 2:
        return candidate
    else:
        return -1



n = int(input())


arr = [int(x) for x in input().split()]


result = majorityElement(arr)
print(result)
