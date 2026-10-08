fobj = open('C:\\Users\\Admin\\Desktop\\Python Traning\\3rd day\\emp.csv','r')
L = fobj.readlines()
fobj.close()

print(type(L),len(L))
print("") # empty line
print("Display file content")
print(L)