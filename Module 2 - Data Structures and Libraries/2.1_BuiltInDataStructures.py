#this module entry is incomplete



# Lists


myListOfStrings = ["here", "is", "a", "list"]
myListOfIntegers = [1, 2, 3, 4]
myListOfFloats = [1.1, 1.2, 1.3, 1.4, 1.5]
# Items contained in a list must all be of the same data type

# Lists can be printed, and will display in list form unless formatted
print(myListOfStrings)
print(myListOfIntegers)
print("You can also get the length " + str(len(myListOfIntegers)))

# Lists can be indexed just like strings
print(myListOfStrings[0])
print(myListOfIntegers[-1])

# Unlike strings, lists are mutable, meaning they can be changed during their lifetime
myListOfStrings[0] = "this"
print(myListOfStrings)
# You can even change a range
myListOfFloats[2:4] = [1.12, 1.13, 1.14, 1.15, 1.16]
print(myListOfFloats)

# We can also add to the list
myListOfStrings.append("!") #append an item to the end
myListOfStrings += ["!"] #concatenate two lists
# Note there are now two exclamation marks in the list
print(myListOfStrings)
print()

# List variables are references to list objects 
# If two variables use the same list, modifications will apply to both
newList = myListOfIntegers
print(newList)
myListOfIntegers += [5, 6]
print(newList)
print(myListOfIntegers)

# Slicing operations create a new list
newList = myListOfIntegers[0:4]
print(newList)
print(myListOfIntegers)

# You can also create lists of lists, each list can be a different data type
myListOfLists = [[1,2,3], ["4","5","6"]]
print(myListOfLists)

# To access members of a list of lists
print("The second item of the first list is " + str(myListOfLists[0][1]))
