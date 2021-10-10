#max of 3 numbers
n1 = int(input())
n2 = int(input())
n3 = int(input())
if n1 < n2:
    n1 = n2
if n1 < n3:
    n1 = n3
print(n1)