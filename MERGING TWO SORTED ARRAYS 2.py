def mergarr(a, b):
    s1 = len(a)
    s2 = len(b)
    
    # Initialize pointers and the result array
    i = 0
    j = 0
    res = []
    
    # Merge elements from both arrays in sorted order
    while i < s1 and j < s2:
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
            
    # Append any remaining elements from array 'a'
    while i < s1:
        res.append(a[i])
        i += 1
        
    # Append any remaining elements from array 'b'
    while j < s2:
        res.append(b[j])
        j += 1
        
    # Print the final merged array elements separated by spaces
    print(*(res))


# --- HACKERANK 4-LINE INPUT FIELD ---

# Line 1: Size of first array (n)
n = int(input())

# Line 2: Elements of first array
a = [int(x) for x in input().split()]

# Line 3: Size of second array (m)
m = int(input())

# Line 4: Elements of second array
b = [int(x) for x in input().split()]


# Run the function
mergarr(a, b)
