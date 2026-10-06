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
hosts = [] 
print(f"Number of elements in the list:{len(hosts)}")

c = 0
while c < 5:
    h = input("Enter a hostname:")
    hosts.append(h) 
    c = c + 1

print(f"\nNumber of elements in the list:{len(hosts)}") 

for var in hosts:
    print(var) 
    

host_name  = input("Enter a hostname:")
if host_name in hosts:
    hosts[-1] = host_name 
else:
    hosts.append(host_name) 
print("\n") # empty line
for var in hosts:
    print(var) 
    