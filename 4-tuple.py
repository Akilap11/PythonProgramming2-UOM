import sys
#list,tuple-ordered, sets-unordered
#python data types-list,tuple,range
#tuples immutable

tuple_1=('a',20,5.1)  #()paranthesis
print(type(tuple_1))

tuple_2='a',20,5.1    #without ()
print(type(tuple_2))  

tuple_3=('mora')
print(type(tuple_3))

tuple_3=('a',)
print(type(tuple_3))

#similar to lists
my_tup=(25,20,34,12,45)
print(my_tup[0])
print(my_tup[4])

#negative indexing like lists
print(my_tup[-1])
print(my_tup[-5])

#slicing
print(my_tup[0:3])  #0 to 2 values

#nested tuples
tup=((1,2),('a','b'))
print(tup[0])
print(tup[1])
print(tup[0][1])

#tuple packing and unpacking
tup2=('car','pen','ice')
a,b,c=tup2
print(b)

#cant insert,delete,update tuples like lists
#so lists are more versatile
#tupples consume less memory, dictionary lot, lists medium

my_tupp=(1,2,3)
my_list=[1,2,3]
my_dict={1,2,3}
print(sys.getsizeof(my_tupp))
print(sys.getsizeof(my_list))
print(sys.getsizeof(my_dict))

#length
print(len((1,2,3)))

#concatenation
a=(1,2,3)
b=(4,5,6)
print(a+b)

#repetition
print(('HI',)*4)

#membership
print(3 in (1,2,3))
print(4 in (1,2,3))

#iteration
for x in(1,2,3):
    print(x)

a = ([1, 2], (3, 4))
a[0][0] = 5
print(a)



