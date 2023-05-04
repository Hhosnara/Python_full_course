mydict = {"name": "Anha", "age": 25, "city":"Dhaka"}
print(mydict)

mydict.popitem()
print(mydict)

if "name" in mydict:
    print(mydict["name"])

    try:
        print(mydict["name"])
    except:
        print("Error")

    mydict_cpy = mydict
    print(mydict_cpy)
    print(mydict)

    mydict_cpy = dict[mydict]
    mydict_cpy["email"] = "hhosnara17@gmail.com"

    print(mydict_cpy)
    print(mydict)

mydict = {"name": "Anha", "age": 25, "city":"Dhaka", "email":"max@xyz.com"}


