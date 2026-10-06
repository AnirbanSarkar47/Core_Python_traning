'''
s = '123456789'
Given string s,
Write a python program calculate sum of the digits.
use: for loop.
'''
s = '123456789'
total = 0
for var in s:
    total = total + int(var) 

print(f"Sum of the digits in string s is:{total}")