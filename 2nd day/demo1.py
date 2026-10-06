'''
Write a python program:
i. create an empty list
ii.display number of elements in the list # use len() function # -> 0
|
iii. use while loop - limit is 5
    a -> read a hostname from user input
    b -> append the hostname to the list
iv. display number of elements in the list # use len() function # ->5
|
v. use for loop - iterate through the list
|
vi. read a hostname from <STDIN>
vii. test input hostname is existing or not in the list
                             |          ===================
viii.                        modify the hostname        |__add the hostname 
                                |__last Index 
                                
ix. display the list of hostnames - use for loop

'''




myList = []
print("Number of elements in the list:", len(myList))

c=5
while 0 < c:
    myList.append(input("Enter an element: "))
    c -= 1

print("Number of elements in the list:", len(myList))

d=5
a=0
while a < len(myList):
    print("Element at index", d, "is", myList[a])
    a += 1


hostname = input("Enter a hostname to check: ")
if hostname in myList:
    print("Hostname exists in the list.")
    index = myList.index(hostname)
    new_hostname = input("Enter the new hostname to replace it: ")
    myList[index] = new_hostname
else:
    print("Hostname does not exist in the list.")
    myList.append(hostname)

print("List of hostnames:")
for i, host in enumerate(myList):
    print("Element at index", i, "is", host)