mytuple = ("Anha", 25 , "Dhaka")
print(mytuple)

item = mytuple[0]
print(item)

for i in mytuple:
    print(i)
    

my_tuple = ("A", "P", "P", "L", "E")
print(my_tuple.index("P"))

my_list = list(my_tuple)
print(my_list)
my_tuple1 = tuple(my_list)
print(my_tuple1)

# slicing tuples
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b =a[::2]
print(b)

my_tuple = (0, 1, 2, 3, 4)

i1, *i2, i3 = my_tuple

print(i1)
print(i2)
print(i3)

































