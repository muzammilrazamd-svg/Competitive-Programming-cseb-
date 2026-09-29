# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read dividend and divisor from STDIN
dividend, divisor = map(int, input().split())

# Compute integer quotient truncated toward zero
quotient = int(dividend / divisor)

# Handle 32-bit integer overflow and underflow constraints
if quotient > 2147483647:
    print(2147483647)
elif quotient < -2147483648:
    print(-2147483648)
else:
    print(quotient)
