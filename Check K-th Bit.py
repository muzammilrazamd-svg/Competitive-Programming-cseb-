import sys

def main():
    # Read all tokens from standard input regardless of line breaks
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    k = int(input_data[1])

    # Check if the k-th bit is set (1) using bitwise AND
    if (n & (1 << k)) != 0:
        print(1)
    else:
        print(0)

if __name__ == '__main__':
    main()
