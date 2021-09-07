# Data Types

'''String'''

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

#String length
print("Length of string: ",len(_str_access))

#String slicing
print("Sliced string: ", _str_access[2:5])

#String Update
_update_str_access = "Hello People"
print("Updated String: "+_update_str_access)

#String deletion
'''del(_update_str_access)
print(_update_str_access)'''
'''del will delete entire string.'''

#String format
_format1_str = "{a} {b} {c}".format(c=" coding ", a=" Welcome ", b=" to ")
print(_format1_str)
_format2_str = "{}{}{}".format("Hello ", "World", "!")
print(_format2_str)
integer = 12.3431
print("Formation in 3.2% format: ")
print('Result: %3.2f' %integer)


'''List'''

#List creation

_list1 = [1,2,3,'Hello','people','@','coding',44,'.com']
print(_list1)

#size or length of List
print("Length of string:",len(_list1))

#Adding Elements
#Append
_list1.append('Added Item')
print(_list1)
_list1.append(('Added Tuple1, Added Tuple2'))
print(_list1)
for i in range(4,8):
    _list1.append(i)
print(_list1)
_list2 = ['Another','List']
_list1.append(_list2)
print(_list1)

#Extend
_list2.extend(['Extended','list'])
print(_list2)

#insert
_list2.insert(4,'inserted')
print(_list2)

#Remove
_list2.remove('inserted')
print("removed",_list2)

#even square
_square_even = []
for i in range(1,10):
    if i%2!=1:
        _square_even.append(i*i)
print("Even square: ",_square_even)

#Odd square
_square_odd = [x*x for x in range(1,10) if x%2==1]
print("Odd square: ", _square_odd)