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

"""
solution
"""
def PlusOne(digits):
    num = 0
    for i in range(len(digits)):
        num += digits[i] * pow(10, len(digits)-1-i)
    return [int(1) for i in str(num + 1)]

