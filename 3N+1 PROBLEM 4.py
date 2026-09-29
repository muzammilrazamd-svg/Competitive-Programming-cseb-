# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

# Cache to store previously computed cycle lengths for dynamic programming optimization
memo = {1: 1}

def get_cycle_length(n):
    if n in memo:
        return memo[n]
    
    path = []
    curr = n
    
    # Store intermediate values until we hit a cached state
    while curr not in memo:
        path.append(curr)
        if curr % 2 == 0:
            curr //= 2
        else:
            curr = 3 * curr + 1
            
    # Backtrack and populate cache
    base_length = memo[curr]
    for step, val in enumerate(reversed(path), start=1):
        memo[val] = base_length + step
        
    return memo[n]

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    i, j = int(input_data[0]), int(input_data[1])
    low, high = min(i, j), max(i, j)
    
    max_len = max(get_cycle_length(k) for k in range(low, high + 1))
    
    print(f"{i} {j} {max_len}")

if __name__ == "__main__":
    solve()
