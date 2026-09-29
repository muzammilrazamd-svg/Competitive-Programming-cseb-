# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def find_triplets():
    # Read all tokens from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    arr = [int(x) for x in input_data[1:1 + n]]
    target = int(input_data[1 + n])

    # Sort the array to easily handle unique triplets and use the 2-pointer technique
    arr.sort()
    
    found = False

    # Fix the first element arr[i]
    for i in range(n - 2):
        # Skip duplicate values for the first element
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum == target:
                print(f"{arr[i]} {arr[left]} {arr[right]}")
                found = True

                left += 1
                right -= 1

                # Skip duplicate values for the second element
                while left < right and arr[left] == arr[left - 1]:
                    left += 1

                # Skip duplicate values for the third element
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1

            elif current_sum < target:
                left += 1
            else:
                right -= 1

    if not found:
        print("No Triplet Found")

if __name__ == '__main__':
    find_triplets()
