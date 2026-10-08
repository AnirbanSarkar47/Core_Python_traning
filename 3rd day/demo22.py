wobj = open("r1.log","w")
wobj.write("Sample data\n")
wobj.write("Product name is:pA Cost is:4565\n")
pname = 'pB'
pcost = 35523.23
wobj.write(f'Product name is:{pname} Cost is:{pcost}\n')
wobj.write('---------------------------------\n')
wobj.close()