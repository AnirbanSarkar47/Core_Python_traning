def file_read():
    fobj = open('r1.log','r')
    s = fobj.read()
    fobj.close()
    print("file contents:-")
    print(s)
    print("End of the function block")
    
def calculate_sales_cost():
    total = 0
    for var in [10,20,30,40,50]:
        total = total + var
    print(f"Sum of cost is:{total}")
    
    
print("-- This is Main block")
file_read()
print("")
calculate_sales_cost()
print("")
if(True):
    file_read()
print("End of the script")