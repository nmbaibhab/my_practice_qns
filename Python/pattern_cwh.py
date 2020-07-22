#program to print pattern 
#codewithharry ex qn-4
"""
if true:(n=3)
*
**
***
if false(n=3)
***
**
*
"""

def pattern1(num):
    for i in range(num+1):
        for j in range(i):
            print("*",end=" ")
        print("\n")

def pattern2(num):
    for i in range(num+1):
        for j in range((num+1)-i):
            print("*",end=" ")
        print("\n")

print("ENter the number ofrows fror  pattern")
num=int(input())
print("INput 1 or 0 to make pattern")
a=int(input())
if bool(a)==True:
    pattern1(num)
else:
    pattern2(num)




