# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def divide_binary_search(x, y):
    # Handle division by zero
    if y == 0:
        return "Division by zero"
    
    # Determine the sign of the result
    is_negative = (x < 0) ^ (y < 0)
    
    # Work with absolute values
    x_abs = abs(x)
    y_abs = abs(y)
    
    # Binary search to find x // y
    low = 0
    high = x_abs
    ans = 0
    
    while low <= high:
        mid = (low + high) // 2
        
        # Check if mid * y_abs <= x_abs
        if mid * y_abs <= x_abs:
            ans = mid          # Valid quotient, store it
            low = mid + 1      # Try to find a larger quotient
        else:
            high = mid - 1     # mid is too large, search smaller values
            
    # Apply sign
    return -ans if is_negative else ans

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    x = int(input_data[0])
    y = int(input_data[1])
    
    result = divide_binary_search(x, y)
    print(result)

if __name__ == '__main__':
    main()
