fobj = open('C:\\Users\\Admin\\Desktop\\Python Traning\\3rd day\\emp.csv','r')
s = fobj.read()
fobj.close()

print(type(s),len(s))
print("") # empty line
print("Display file content")
print(s)