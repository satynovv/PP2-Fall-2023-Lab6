import math
def trapezoid(a, b, h):
    area=1/2*(a+b)*h
    return area
a=int(input())
b=int(input())
h=int(input())
area=trapezoid(a, b, h)
print(area)