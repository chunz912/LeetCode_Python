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