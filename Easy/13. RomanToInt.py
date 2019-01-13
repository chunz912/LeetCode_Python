
"""solutioin"""
def romanToInt(self, s):
    roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    z = 0
    for i in range(0, len(s) - 1):
        if roman[s[i]] < roman[s[i+1]]:
            z -= roman[s[i]]
        else:
            z += roman[s[i]]
    return z + roman[s[-1]]
"""
Note: The trick is that the last letter is always added. 
Except the last one, if one letter is less than its latter one, this letter is subtracted.
"""


"""
My solution
"""


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

