import pprint
products = {}  
products['id'] = [101,102,103]
products['names'] = ['pA','pB','pC']
products['cost'] = [1000,2000,3000]
products['Qty'] = [10,20,30]
pprint.pprint(products)

print('\n') 




products=[] 
products.append({'id':101,'names':'pA','cost':1000,'Qty':10})
products.append({'id':102,'names':'pB','cost':2000,'Qty':20})
products.append({'id':103,'names':'pC','cost':3000,'Qty':30})
pprint.pprint(products)
print("\n") 




products = {} 
products['id'] = {'id1':101,'id2':102,'id3':103}
products['names'] = {'name1':'pA','name2':'pB','name3':'pC'}
products['cost'] = {'cost1':1000,'cost2':2000,'cost3':3000}
products['Qty'] = {'Qty1':10,'Qty2':20,'Qty3':30}
pprint.pprint(products)