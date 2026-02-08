#this module entry is incomplete



# Lists


my_list_of_strings = ["here", "is", "a", "list"]
my_list_of_integers = [1, 2, 3, 4]
my_list_of_floats = [1.1, 1.2, 1.3, 1.4, 1.5]
# Items contained in a list must all be of the same data type

# Lists can be printed, and will display in list form unless formatted
print(my_list_of_strings)
print(my_list_of_integers)
print("You can also get the length " + str(len(my_list_of_integers)))

# Lists can be indexed just like strings
print(my_list_of_strings[0])
print(my_list_of_integers[-1])

# Unlike strings, lists are mutable, meaning they can be changed during their lifetime
my_list_of_strings[0] = "this"
print(my_list_of_strings)
# You can even change a range
my_list_of_floats[2:4] = [1.12, 1.13, 1.14, 1.15, 1.16]
print(my_list_of_floats)

# We can also add to the list
my_list_of_strings.append("!") #append an item to the end
my_list_of_strings += ["!"] #concatenate two lists
# Note there are now two exclamation marks in the list
print(my_list_of_strings)
print()

# List variables are references to list objects 
# If two variables use the same list, modifications will apply to both
newList = my_list_of_integers
print(newList)
my_list_of_integers += [5, 6]
print(newList)
print(my_list_of_integers)

# Slicing operations create a new list
newList = my_list_of_integers[0:4]
print(newList)
print(my_list_of_integers)

# You can also create lists of lists, each list can be a different data type
myListOfLists = [[1,2,3], ["4","5","6"]]
print(myListOfLists)

# To access members of a list of lists
print("The second item of the first list is " + str(myListOfLists[0][1]))









# Tuples


point = (0,7)


match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")


