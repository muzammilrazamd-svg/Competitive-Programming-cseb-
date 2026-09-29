def max_sub_arr(arr):
    max_sum=0
    cur_sum=0
    for num in arr:
        cur_sum=max(0,cur_sum+num)
        
        max_sum=max(cur_sum,max_sum)
        
    print(max_sum)


# 1. Read the first line (the size of the array)
n = int(input())

# 2. Read the second line (the space-separated numbers)
arr = [int(x) for x in input().split()]


max_sub_arr(arr)
