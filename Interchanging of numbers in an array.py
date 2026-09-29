# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read the number of elements
n = int(input())

# Read the space-separated integers into a list
arr = list(map(int, input().split()))

# Find the indices of the minimum and maximum values
# Using .index() gets the first occurrence of min and max elements
min_idx = arr.index(min(arr))
max_idx = arr.index(max(arr))

# Swap the elements
arr[min_idx], arr[max_idx] = arr[max_idx], arr[min_idx]

# Print the modified array separated by spaces
print(*arr)
