# Enter your code here. Read input from STDIN. Print output to STDOUT
def maxAscendingSum(arr):
  
    max_sum = arr[0]
    current_sum = arr[0]
   
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            current_sum+=arr[i]
        else:
            
            max_sum = max(max_sum, current_sum)
            current_sum = arr[i]
            
    
    return max(max_sum, current_sum)

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    if data:
        n = int(data[0])
        arr = [int(x) for x in data[1:n+1]]
        print(maxAscendingSum(arr))
