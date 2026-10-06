name = input("Enter name :")
age = input(f"Enter {name}'s age :")
cost = input(f"Enter {name} cost :")
# login_status = input("Enter login status :")


print("Name:", name)
print("Age:", age)
print("Cost:", cost)
print("Login Status:", True)
print(f"18% Tax : {float(cost) * 0.18}")
print(f"Total Cost with Tax : {float(cost) + (float(cost) * 0.18)}")

