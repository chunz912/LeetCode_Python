"""
my solution
"""

def PlusOne(digits):
    num = ""
    for i in digits:
        num += str(i)
    new_num = str(int(num) + 1)
    out = []
    for j in range(len(new_num)):
        digit = int(new_num[j])
        out.append(digit)
    return out