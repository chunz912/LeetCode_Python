"""
my solution
"""
def lengthOfLastWord(s):    
    s = s.rstrip()
    if len(s) == 0:
        return 0
    rev_s = s[::-1]
    for i in range(0, len(s)):
        if rev_s[i] == " ":
            return i
            break
        else:
            continue
    return i+1

"""
solution
"""
def lengthOfLastWord(s): 
    return len(s.rstrip(' ').split(' ')[-1])

def lengthOfLastWord(s): 
    return 0 if len(s.split() == 0) else len(s.split()[-1])
