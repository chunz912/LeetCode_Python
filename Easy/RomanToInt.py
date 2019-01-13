""" My solution"""


def romanToInt(s):
    roman = {"I":1, "V":5, "X":10, "L": 50, "C":100, "D":500, "M":1000}
    z = 0
    m = 0
    i = 0
    if len(s) == 1:
        z = roman[s]
        return z
    else: 
        while i < len(s) - 1:
            if roman[s[i]] >= roman[s[i+1]]:
                z += roman[s[i]]
                i += 1
            else:
                m = roman[s[i+1]] - roman[s[i]]
                z += m
                i += 2
        if roman[s[-2]] >= roman[s[-1]]:
            z = z + roman[s[-1]]
            return z
        else:
            return z
