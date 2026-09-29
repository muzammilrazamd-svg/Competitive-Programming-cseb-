a, b = map(int, input().split())

# Bitwise addition using XOR for sum and AND + shift for carry
while b != 0:
    carry = a & b   # Carry contains common set bits of a and b
    a = a ^ b       # XOR sums bits of a and b where at least one is not set
    b = carry << 1  # Carry is shifted by one so that adding it to a gives the required sum

print(a)
