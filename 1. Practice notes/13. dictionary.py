#DICTIONARY

#do not allow duplicates
#duplicates will overwrite the existing value
#any type of data can be stored
#a={"keys": values}


a={
    "name":"Ram",         
    "age":21,                 #integers are represented without ""
    "subjects":["cs","maths","english"],
    "marks":[9,9,8]
}    #keys  #values

print(a)    #prints the dictionary

print(a.keys())   #print the keys of the dictionary
print(a.values()) #print the values of the dictionary


a["color"]="Red"  #adds another key:value pair
print(a)


a["age"]=23  #modifying values
print(a)
#or
a.update({"age":23})


a.pop("subjects")  #removes the subject key and its values
print(a)
#or
del a["age"]
print(a)


a.clear()  #clears all the keys and values inside the dictionary
print(a)

del a #deletes whole dictionary