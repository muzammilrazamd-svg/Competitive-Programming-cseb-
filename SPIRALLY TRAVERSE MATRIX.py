# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    matrix = []
    idx = 2
    for i in range(N):
        row = []
        for j in range(M):
            row.append(int(input_data[idx]))
            idx += 1
        matrix.append(row)
        
    top, bottom = 0, N - 1
    left, right = 0, M - 1
    
    result = []
    
    while top <= bottom and left <= right:
        # Traverse Left to Right across the top row
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        
        # Traverse Top to Bottom along the right column
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        # Traverse Right to Left across the bottom row
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
            
        # Traverse Bottom to Top along the left column
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
            
    print(*(result))

if __name__ == "__main__":
    main()
