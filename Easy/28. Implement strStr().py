# -*- coding: utf-8 -*-
"""
solution
"""

def strStr(self, haystack, needle):
    for i in range(len(haystack)-len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

"""
采用brute force方式，即依次从字符串的每个位置开始，截取和子字符串相同长度的字符串，与给定的子字符串进行比较。
"""
