# fibonacci.py

Fmax = 100
a, b = 0, 1

while a < Fmax:
    print(b, end=' ')
    a, b = b, a+b
print()         
