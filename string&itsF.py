String1 = "AarthSoftware"
print(String1)
#  Program to Access characters of String
# Printing First character
print("\nFirst character of String is: ")
print(String1[0])
#Program to reverse a string
print(String1[::-1])
# Reverse the strinh using reversed and join function
String1 = "".join(reversed(String1))
# Printing 3rd to 12th character
print("\nSlicing characters from 3-12: ")
print(String1[3:12])
# Updating a character of the String
## As python strings are immutable, they don't support item updation directly
# Python Program to Update
# entire String
String = "AarthSoftware"
print("Initial String: ")
print(String)
# Updating a String
String = "Welcome to the Geek World"
print("\nUpdated String: ")
print(String)
# Formatting of Strings
String1 = "{} {} {}".format('Geeks', 'For', 'Life')
print("Print String in default order: ")
print(String1)
# Positional Formatting
String1 = "{1} {0} {2}".format('Geeks', 'For', 'Life')
print("\nPrint String in Positional order: ")
print(String1)
# Keyword Formatting
String1 = "{l} {f} {g}".format(g='Geeks', f='For', l='Life')
print("\nPrint String in order of Keywords: ")
print(String1)
