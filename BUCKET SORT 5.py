# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def bucket_sort():
    # Read all input from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    raw_numbers = input_data[1:]

    # Check if the inputs are integers or floats based on the presence of a decimal point
    is_float = any('.' in num for num in raw_numbers[:10])

    if is_float:
        # Convert to float and sort
        arr = [float(x) for x in raw_numbers]
        arr.sort()
        # Print numbers formatted to 2 decimal places
        print(" ".join(f"{x:.2f}" for x in arr))
    else:
        # Convert to int and sort
        arr = [int(x) for x in raw_numbers]
        arr.sort()
        # Print integers standard output
        print(" ".join(map(str, arr)))

if __name__ == '__main__':
    bucket_sort()
