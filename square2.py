import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
d = b*b - 4*a*c
x1 = 0
x2 = 0

if d > 0:
    x2 = (d**(1/2) - b) / (2*a)
    x1 = ((d**(1/2))*(-1) - b) / (2*a)
    print(int(x1), int(x2))
elif d == 0:
    x1 = (b / (2 *a)) * (-1)
    print(int(x1), int(x1))
else:
    print("Equation has no solution")
