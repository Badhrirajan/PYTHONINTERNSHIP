1.Write a program to create a list of n integer values and do the following
  Add an item in to the list (using function)
  Delete (using function)
  Store the largest number from the list to a variable
  Store the Smallest number from the list to a variable

2) Create a tuple and print the reverse of the created tuple
3) Create a tuple and convert tuple into list

EXERCISE:1
a=['apple','banana','mango','pear','papaya']
a.append('orange') #adding item using function
print(a)
a.remove(banana) #deleting item using function
print(a)

a=[10,15,25,35,60,75,90]
a.sort()
print("Largest Item in the list is:",a[-1])
print("Smallest Item in the list is:",a[0])

EXERCISE:2
a=['apple','mango','papaya','banana']
b=reversed(a)
print(tuple(b))

EXERCISE:3
a=['banana','apple','orange','pineapple']
b=list(a)
print(b)
