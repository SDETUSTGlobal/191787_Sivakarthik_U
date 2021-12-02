#len method
Dict = {'tim':18,'Charlie':12,'Tiffany':22,'Robert':25}
print("Length : %d" % len(Dict))
#variable space
Dict = {'tim':18,'Charlie':12,'Tiffany':22,'Robert':25}
print("Variable Type : %s" % type(Dict))
#str method
Dict = {'tim':18,'Charlie':12,'Tiffany':22,'Robert':25}
print("Printable String: %s" % str(Dict))
#merge dictionary
my_dict1 = {"username":"XYZ","email": "xyz@gmail.com","location":"Mumbai"}
my_dict2 = {"firstname":"Siva","Lastname":"U"}
my_dict1.update(my_dict2)
print(my_dict1)
#merge dictionary ** method -kwargs
my_dict1 = {"username":"XYZ","email": "xyz@gmail.com","location":"Mumbai"}
my_dict2 = {"firstname":"Siva","Lastname":"U"}
my_dict = {**my_dict1,**my_dict2}
print(my_dict)
#dictionary membership test
my_dict = {"username": "XYZ", "email": "xyz@gmail.com", "location":"Mumbai"}
print("email" in my_dict)
print("location" in my_dict)
print("test" in my_dict)
print("username" in my_dict)
#append dictionary
my_dict = {"Name":[],"Address" : [],"Age" : []};
my_dict["Name"].append("Guru")
my_dict["Address"].append("Mumbai")
my_dict["Age"].append(50)
print(my_dict)
#accessing diictionary elements
my_dict = {"username": "XYZ", "email": "xyz@gmail.com", "location":"Mumbai"}
print("username :",my_dict["username"])
print("email :",my_dict["email"])
print("location :",my_dict["location"])
#deletinf dictionary
my_dict1 = {"username": "XYZ", "email": "xyz@gmail.com", "location":"Mumbai"}
del my_dict1["username"]
print(my_dict1)
my_dict1.clear()
print(my_dict1)
del(my_dict1)
print(my_dict1)
#deletion with pop method
my_dict2 = {"username": "XYZ", "email": "xyz@gmail.com", "location":"Mumbai"}
my_dict2.pop("Username")
print(my_dict2)
#append elements in dictionary
my_dict3 = {"username": "XYZ", "email": "xyz@gmail.com", "location":"Mumbai"}
my_dict3['name']='Siva'
print(my_dict3)
#update existing elements in dictionary
my_dict = {"username": "XYZ", "email": "xyz@gmail.com", "location":"Mumbai"}
my_dict["username"]="Siva"
print(my_dict)
#insert one dictionary into another
my_dict = {"username": "XYZ", "email": "xyz@gmail.com", "location":"Mumbai"}
my_dict1={"firstname" : "ABC", "lastname" : "DEF"}
my_dict["name"] = my_dict1
print(my_dict)

