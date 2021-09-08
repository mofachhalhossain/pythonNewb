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


'''Tuples'''

_tuple1 = (1,2,3)
print('Initial tuple: ', _tuple1)
_tuple1 = tuple('hello')
print('Added Elements: ',_tuple1)

#Creating tuples with nested tuples with differnt data types
_tuple_int = (5,6,7,8)
_tuple_str = ('Hello', 'world', '!')
_tuple_mix = _tuple_int,_tuple_str
print("Mixed tuple: ",_tuple_mix)

_tuple_list = ([])
for i in range(1,6):
    _tuple_list.append(i)
print("List tuple: ", _tuple_list)

#tuple concat
_tuple_concat = _tuple_int+_tuple_str
print("Concat : ", _tuple_concat)


'''Dictionary'''

_dictionary = {1: 'Welcome', 2: 'to', 3: 'python', 4: 'world'}
print(_dictionary)
_dictionary2 = dict([(1,'hello'), (2,'World')])
print(_dictionary2)

#Nested dictionary
_nested_dictionary = {1: 'Hello', 2: 'I\'m', 3:{'a': 'nested ', 'b': 'dictionary'}}
print(_nested_dictionary)

#update dictionary
_update_dictionary = {3: {'a': 'updated', 'b': 'dictionary'}}
_nested_dictionary.update(_update_dictionary)
print(_nested_dictionary)

#Accessing Element from dictionary
print('Accessing element: ',_nested_dictionary[3])
_access_element = _nested_dictionary.get(2)
print('Access element by get: ',_access_element)

#Deleting Element from dictionary
_del_dictionary = {1: 'One', 2: 'Two', 3: "Three", 4: 'Four', 5: 'Five'}
print("Initial dictionary: ", _del_dictionary)
del _del_dictionary[3]
print("After deleting: ", _del_dictionary)

#pop
_del_dictionary.pop(4)
print('pop dictionary element: ',_del_dictionary)

#popitem()
_item_deleted = _del_dictionary.popitem()
print("After pop",_del_dictionary)
print("item deleted: ", _item_deleted)


'''Array'''

#creating array
import array as arr
a = arr.array('i',[1,2,3,4,5])
print("array: ", end='')
for i in range(0,5):
    print(a[i], end=' ')

#accessing/searching element
print("\nAccessing element 4: ", a[4])

#updating element
a[2] = 6
print("Update: ", end='')
for i in range(0,5):
    print(a[i], end=' ')

#slicing array
import array as array
b = array.array('d', [1.1,2.2,3.3,4.4,5.5])
_sliced_array = b[0:3]
print("\nsliced array: ")
for i in range(0,5):
    print(b[i])