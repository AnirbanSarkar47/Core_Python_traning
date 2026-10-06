port = input("Enter port: ")

if(5001 <= float(port) and float(port) <= 5999):
    appname="flask"
else:
    appname= "webApp"


print(f"App Name: {appname} running on port {port} ")