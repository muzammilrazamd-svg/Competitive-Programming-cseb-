# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def solve():
    # Read all input from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    # Parse sizes and elements
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Extract the two sorted arrays
    arr1 = [int(x) for x in input_data[2 : 2 + n]]
    arr2 = [int(x) for x in input_data[2 + n : 2 + n + m]]
    
    # Merge and sort the arrays
    merged = sorted(arr1 + arr2)
    total_len = n + m
    
    # Calculate median
    if total_len % 2 != 0:
        # Odd total length: middle element
        median = float(merged[total_len // 2])
    else:
        # Even total length: average of the two middle elements
        mid1 = merged[(total_len // 2) - 1]
        mid2 = merged[total_len // 2]
        median = (mid1 + mid2) / 2.0
        
    # Print formatted to 1 decimal place
    print(f"{median:.1f}")

if __name__ == '__main__':
    solve()
