"""
solution
"""

def longestCommonPrefix(strs):
    if not strs:
        return ""
            
    for i, letter_group in enumerate(zip(*strs)):
        if len(set(letter_group)) > 1:
            return strs[0][:i]
            
    else:
        return min(strs)

    
"""
shorter version
"""

def longestCommonPrefix(self, strs):        
        i = 0
        for x in zip(*strs):            
            if len(set(x)) > 1: return strs[0][:i]            
            i += 1            
        return strs[0][:i] if strs else ''
    
    
"""
already implemented in Python
"""

def longestCommonPrefix(self, strs):
    return os.path.commonprefix(strs)



