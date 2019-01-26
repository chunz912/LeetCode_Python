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
We're given a list of digits, and the idea here is to convert that list to an integer, num. 
So each digit is multiplied by the proper place value and added to num. 
For example, if digits = [3, 8, 2, 5] then on the first iteration 3 is multiplied by 10 to the power of 4-1-0 = 3, 
so this results in 3000, which is added to num. Then 8 is multiplied by 10^2 and added to num, and so on.

The last step is to add 1 to num, convert it to a list and return that list.
"""
def PlusOne(digits):
    num = 0
    for i in range(len(digits)):
        num += digits[i] * pow(10, len(digits)-1-i)
    return [int(1) for i in str(num + 1)]

