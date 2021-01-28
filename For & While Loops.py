#1. write a program using for loop  to find the sum of all numbers stored in a list
x = 0
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
for y in numbers:
#x = x + y
  x += y
print(x)

#2, write a program using for loop to print squares of all numbers present in a list
numbers = [1, 2, 4, 6, 11, 20]
for x in numbers:
#print(x,'=',x*x)
    print(x,'=', x**2)

#3. Write a program using while loop & for loop to print list of all fruits
fruits = ["apple", "orange", "kiwi"]
for x in fruits:
    print (x)


#4. Write a program using a while loop to print any number table; example 10 * 1 = 10, 10 * 2 = 20 ............. 10 * 10 = 100.

thislist = [1,2,3,4,5,6,7,8,9,10]
y = 10
for x in thislist:
    print(y, '*', x, '=', x*y)

#5. Write a program using while loop to print factorial of any given number ; eg 5 factorial = 5 * 4 * 3 * 2 * 1 = 120
thislist = [1,2,3,4,5,6,7]
fact = 1
for x in thislist:
    fact = fact * x
    print (fact)
print ('fact =', fact)

#6. Write a program using for loop that iterate over the string and print each character in that string
#testStr = 'HELLO'
for x in "HELLO":
    print(x)

#7. Write a program using for while & for loop to print the sum of first 5 natural numbers.
x = 0
numbers = [1,2,3,4,5]
for y in numbers:
#x = x + y
  x += y
print(x)
