import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    weights = [int(x) for x in input_data[1:n+1]]
    
    # Sort weights in descending order
    weights.sort(reverse=True)
    
    group1 = []
    group2 = []
    sum1 = 0
    sum2 = 0
    
    max_size = (n + 1) // 2
    
    for weight in weights:
        # Assign to group 1 if it has room and its current sum is smaller
        if len(group1) < max_size and (sum1 <= sum2 or len(group2) == max_size):
            group1.append(weight)
            sum1 += weight
        else:
            group2.append(weight)
            sum2 += weight
            
    print(abs(sum1 - sum2))

if __name__ == '__main__':
    solve()
  
