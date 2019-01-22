# -*- coding: utf-8 -*-
def CountAndSay(n):
    b='1'   #将第一行的1换成字符类型，便于下一行的读出
    for i in range (n-1):    #(n-1)是因为第一行不需要处理，直接可以读出
        a,c,count=b[0],'',0   #a用来读取上一行的第一个字符，c用来存放读出的内容(char)，count用来统计
        for j in b:   
            if a==j:
                count+=1
            else:
                c+=str(count)+a   #注意一定要将count转换为字符型，否则两个数就会相加（变成数学公式）。
                a=j
                count=1
        c+=str(count)+a
        b=c
    return c
