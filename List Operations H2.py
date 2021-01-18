#1. 
thislist = ["apple", "banana", "cherry", "orange", "melon", "mango"]
#- Add item "grapes" at 3rd position
thislist.insert(2, "grapes")
#- Add item "kiwi" at end of the list
thislist.append("kiwi")
print(thislist)

#2  
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
#- use function to append elements from tropical list to the current thislist
thislist.extend(tropical)
print(thislist)

#3. 
thislist = ["apple", "banana", "cherry"]
#- use function to remove item "banana" from the list.
thislist.remove("banana")
print(thislist)

#4. 
thislist = ["apple", "banana", "cherry", "orange", "melon", "mango"]
# - use function to remove third item from  the list
thislist.pop(2)
# - use function to remove last item from the list
thislist.pop()
print(thislist)

#5. 
thislist = ["apple", "banana", "cherry"]
#- use a function to delete the entire list
del thislist

#6. 
thislist = ["apple", "banana", "cherry"]
#- use function to clear list
thislist.clear()
print(thislist)

#7. 
thislist = ["apple", "banana", "cherry", "orange", "melon", "mango"]
#- use function to loop through list items
for x in thislist:
    print(x)

#8. Write a program using a for loop to print any number table; example 10 * 1 = 10, 10 * 2 = 20 ............. 10 * 10 = 100.
thislist = [1,2,3,4,5,6,7,8,9,10]
y = 7
for x in thislist:
    #print(y*x)
    print(y,'*',x, '=', x*y)

#9. Write a program using for loop to print factorial of any given number ; eg 5 factorial = 5 * 4 * 3 * 2 * 1 = 120
thislist = [1,2,3,4,5]
fact = 1
for x in thislist:
    fact = fact * x

print('fact =', fact)

#Thanks for the help on #9
