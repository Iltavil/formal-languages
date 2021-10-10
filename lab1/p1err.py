#error of p2
#gcd of 2 numbers
n1 = int(input())
2n = int(input())
n = 0

while n1 != 2n and n1 != 0 and 2n != 0:
    if n1 > 2n:
        n1 = n1 % 2n
    else:
        2n = 2n % n1
    n++

print(max(n1,2n))