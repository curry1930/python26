#dictionary = a collection of {"key":"value"} pairs
#             ordered and changeable but no duplicates

capitals={"India":"New Delhi",
          "Pakistan":"Islamabad",
          "Nepal":"Kathmandu",
          "Sri Lanka":"Colombo"}

#print(dir(capitals))
#print(help(capitals))

print(capitals.get("Japan"))

#if capitals.get("Japan"):
#    print("That capital does exist!")
#else:
#    print("That capital doesnt exist!")    

#capitals.update({"USA":"Washington D.C"})  adds key and a value pair
#capitals.update({"India":"Gujarat"})       updates the existing key value pair

#capitals.pop("Pakistan")                    deletes a certain key value pair
#capitals.popitem()                          deletes the recent pair of the dictionary
#capitals.clear()                            deletes the whole dic

#keys=capitals.keys()
#print(keys)                                prints all the keys in a list
#for key in capitals.keys():
#    print(key)

#values=capitals.values()
#print(values)                              prints all the values in a list
#for value in capitals.values():
#    print(value)   
 
#items=capitals.items()
#print(items)                                returns a 2D list of tuples 
#for key,value in capitals.items():
#    print(f"{key}:{value}")
