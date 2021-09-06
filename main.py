# Data Types

#String

#String creation
string1 = "I'm string1"
print(string1)
string2 = 'I\'m string2'
print(string2)
string3 = '''I'm
    string3'''
print(string3)

#Accessing String Character
_str_access = "Hello World"
print("Initial String: ", _str_access)
print("Accessing last character: "+_str_access[-1])
print("Accessing first character: "+_str_access[0])

#String slicing
print("Sliced string: ", _str_access[2:5])

#String Update
_update_str_access = "Hello People"
print("Updated String: "+_update_str_access)

#String deletion
'''del(_update_str_access)
print(_update_str_access)'''
'''del will delete entire string.'''