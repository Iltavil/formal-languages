#gcd of 2 numbers
n1 = int(input())
n2 = int(input())

while n1 != n2 and n1 != 0 and n2 != 0:
    if n1 > n2:
        n1 = n1 % n2
    else:
        n2 = n2 % n1

if n1 < n2:
    n1 = n2
print(n1)