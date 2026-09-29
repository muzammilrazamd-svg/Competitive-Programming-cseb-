# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read N and K from input
n, k = map(int, input().split())

# Toggle the K-th bit using the XOR (^) bitwise operator
result = n ^ (1 << k)

# Print the result
print(result)
