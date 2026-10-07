'''
Given List

Emp = ['101,john,sales,1000','102,ram,prod,2000','103,raju,hr,3000','104,bibu,sales,4000']

-> iterate a emp list
-> split each element of the list using ',' as a delimiter
-> display empName in title case and emp department in upper case 
-> calculate sum of emp salary and display the total salary
'''
Emp = ['101,john,sales,1000','102,ram,prod,2000','103,raju,hr,3000','104,bibu,sales,4000']

total = 0
for var in Emp:
    eid,ename,edept,ecost = var.split(',')
    print(f"Emp Name:{ename.title()}\t Emp Dept:{edept.upper()}") 
    total = total +int(ecost)
    
print(f"\nTotal Salary:{total}") 

    