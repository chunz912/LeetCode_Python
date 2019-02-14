# my solution

def mySqrt(x):
    i = 0
    while i <= x:
        if i**2 <= x and (i+1)**2 > x:
            return i
        else:
            i = i+1
