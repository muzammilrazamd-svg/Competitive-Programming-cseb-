# Enter your code here. Read input from STDIN. Print output to STDOUT# Read N from STDIN
n = int(input())

# Count the number of set bits (1s) in binary representation
print(bin(n).count('1'))
