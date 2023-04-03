#Intersection_udpate what is doesa1
#Remove the items that is not present in both x and y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)



#symemetric_diference_update()

#Remove the items that are present in both sets, AND insert the items that is not present in both sets:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

#symmetric_difference()
#Return a set that contains all items from both sets, except items that are present in both sets:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y) 

print(z)

#append() func by converting into a list