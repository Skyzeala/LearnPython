# Here are some things we can do with strings
# We use a lot of print statements here to show the outputs, 
#     but the print statements themselves are not the focus of this file

# Strings are how we can store and use text in Python
# Strings are things like single letters ("a"), words ("Hello"), and sentences too ("Hello, World!")

# Strings can be defined using single quotes or double quotes, these are then called string literals
print('This is a string')
print("This is also a string")
print() #prints an empty new line, this helps to keep the output formatted and easier to read

# We can combine two strings with concatenation, one string after the other 
print('This is a string, and ' + "this is also a string.") #concatenate 2 strings explicitly with +
print("Concatenation is implicit " "for string literals") #concatenate 2 strings implicitly, no plus needed
# In general you will likely want to use the form with the +, as most strings will be stored in variables
#     rather than hardcoded as string literals
print("you can concatenate " + "as many " + "strings " + "together " + "as you'd like"
      + ", and even move to the next line " + "to format the look of your code")
# Splitting a single statement across multiple text lines is called a hanging indent
# Line splits also work with implicit concatenation too
print("When printing long sequences, "
      "we can spread our code across multiple lines "
      "while keeping the output string in tact") 
print()

# We can convert other value types to string form, like numbers, this is called casting, or type casting
print("Here we convert an integer to a string: " + str(5))
# If we tried adding the number 5 to the string without casting, the Python interpreter will give an error 
# We can print data types like this, str stands for string, and int stands for integer
print("String type: " + str(type("my string")))
print("String type: " + str(type(5)))
# There are conversion functions for almost all data types in Python, 
#     but not every type can be converted to every other, sometimes Python will give an error instead

# Strings can be multiplied by whole numbers, which acts as a repeater 
print("multiply!" * 3)
# Try creating some new strings using concatenation and multiplication together
print()

# There are special character sequences that signify a different meaning in strings
#     these are called escaped characters, the escape symbol is a \ 
#     and will attempt to escape the character following it
print("We can specify a newline in a string with \nbackslash n ")
print("We\tcan\talso\ttab with backslash t")
print("We can print backslashes by escaping the backslash with a backslash \\")
print(r"Sometimes we don't want to escape our \characters, so we can use a raw string instead")
print(r"Raw strings are denoted by an r right before the first quotation mark, and are essentially wysiwyg")
print(r"Raw strings are useful for paths like D:\Downloads\code"
      "\nwhere the alternative can be messy to type out D:\\Downloads\\code")
print()

print("Quote symbols also need to be used with special care")
print("You can specify them explicitly by escaping them \" \' ")
print("Or use them freely so long as your 'current string' is not defined by them")
print()

# Large blocks of text involving formatting can be written using triple quotes
print('''
                This is a multi-line string literal, "quotes" don't need to be escaped, but \\ does
            It will output   almost   exactly what is between the 3 consecutive quotes
      If you want to ignore a newline, \
you can escape it, causing the code's newline to be ignored but
This is useful for easy formatting of larger blocks of text
      ''')
print()



# Variables

# Instead of string literals, we can use variables to store strings, variables act as labelled containers for data
my_string = "my string" # The variable my_string is set to the string literal value "my string"
# Note that the "=" here is not used to check for equivalence, it is assignment, my_string variable is being set
print(my_string) # We can now use the variable to print our string
# If the variable changes, the next uses of the variable will have the updated value
my_string = "my string updated"
print(my_string)
# You can use existing variables to create new ones, this won't change the original my_string
another_string = my_string + " into a new string"
print(another_string)

# Variable names are case sensitive, cannot start with a number, and cannot contain whitespace characters
# Variable names can contain numbers, letters, and underscores
# There are also a few keywords that cannot be used as variable names
#     You can find a list of keywords here https://www.w3schools.com/python/python_ref_keywords.asp
# The common Pythonic way of using multi word variables is called snake case, where each word is separated by _

# Python data types are dynamic, they are determined at runtime and not explicitly stated in the code
# Other languages like C required the type of each variable to be specified upon variable creation
# R works similarly to Python

# Multiple variables can be assigned to the same value in a single statement like this
var1 = var2 = var3 = "var"
print(var1 + " " + var2 + " " + var3)

# Multiple variables can be defined with multiple values at once with comma separation
var1, var2, var3 = "one", "two", "three"
print(var1 + " " + var2 + " " + var3)



# In Python, strings can be accessed one character at a time by index
# Python uses zero indexing, which means the first character of a string is at index 0, 
#     the second is at index 1, the third is at index 2, and so on
# The last character of a string will be at the index number which is one less than the length of the string
my_string = "abcdef"
print("The length of my_string is " + str(len(my_string))) #the len function returns the length of my_string
print(my_string[0]) #prints the first character of a string
print(my_string[3]) #print the 4th character
print(my_string[-1]) #print the last character 
print(my_string[-2]) #print the second last character
# Try changing the string and the index numbers to see how the outputs change
print("Individual characters are still of type " + str(type(my_string[0]))) 
# Many other coding languages actually use 'char' as the type for individual characters
print()

# You can get a partial string with substring indexing, also called slicing, here are some examples
my_string = "abcdef"
print(my_string[0:3]) #prints a substring from the first char and up to but not including the 4th char
print(my_string[:3]) #you can actually leave out the initial 0, as the default is the start of the string
print(my_string[2:]) #print the substring starting at index 2, and going to the end of the string
print(my_string[0:-1]) #print everything but the last character of a string
print(my_string[-1:]) #print the last character of a string
# You can use a 3rd number after another colon to signify the step, or interval to slice with
print(my_string[0::2]) #print every other letter starting with index 0

# Modification
# Strings in python are immutable, meaning they cannot be changed after creation
# To get around this, a new string must be made
my_string = "thete is a typo in this statement" #creates an instance of a string, and my_string stores its value
print(my_string)
my_string = my_string[:3] + 'r' + my_string[4:] #creates a new string, and then replaces the value of my_string with it
print(my_string)
# Writing something like 'my_string[3] = "r"' would not work, as we cannot modify an existing string
# What happens on the backend is a new string gets made, and replaces the string stored in the variable
# Eventually Python's garbage collection system will come around and delete the old string from memory

# Each string variable is unique, and changing one will not change another
my_string = "my string"
my_new_string = my_string

print(my_new_string)
my_string = "changed string"
print(my_new_string)
print(my_string)
