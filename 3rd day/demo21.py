fobj = open('C:\\Users\\Admin\\Desktop\\Python Traning\\3rd day\\emp.csv','r')
L = fobj.readlines()
fobj.close()

for var in L:
    print(var.strip()) # strip() removes leading and trailing whitespace characters including newline

print("\n") # empty line
for var in L:
    if 'sales' in var:
        var = var.strip() 
        print(var)
        
print("\n")
total = 0
for var in L:
    if 'sales' in var:
        var = var.strip() 
        eid,ename,edept,eplace,ecost = var.split(",")
        total = total + int(ecost)
        print(f"Emp Name is:{ename.title()}  \t Working Dept is:{edept.upper()}") 

print("-"*35)
print(f"Sum of sales dept emp's cost is:{total}")
print("-"*35) 