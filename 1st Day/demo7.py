# appname = input("Enter app name: ")



# if "flask" in appname.lower():
#     print("Running a Flask app")
# else:
#     print("Running a different app")    























nameOfApp = input("Enter app name : ")



if "flask" in nameOfApp.lower():
    portNumber = 5000
elif "fastapi" in nameOfApp.lower():
    portNumber = 8080
elif "prometheus" in nameOfApp.lower():
    portNumber = 9090
else:
    portNumber = 8000   


print(f"The port number for {nameOfApp} is {portNumber}")