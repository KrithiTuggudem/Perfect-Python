import keyword
print(keyword.kwlist)

#1. Write a program using while loop to print all even numbers from 1 to 100.
for i in range (100):
    if i % 2 == 0:
        print (i, "is an even number")

#2. Write a program using while loop to print all odd numbers from 1 to 100.
for i in range (100):
    if i % 2 == 1:
        print (i,"is an odd number")

#3. Write a program using while loop to print all prime numbers from 1 to 100.
num = 100
for i in range(2, num):
    if num % i == 0:
        print('not a prime')
        break
else:
    print('prime') 

# I do not know what to do for #3. It is only doing it for one number at a time.
#  I loked up how to do it here is what I got:
for Number in range (1, 101):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
            break

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')

#Can you please explain in class?

#4. Write a program to calculate perimeter of the triangle s1 = 10, s2 = 20, s3 = 30
s1 = 10 
s2 = 20 
s3 = 30
x = s1 + s2 + s3
print(x)


#5
a = 33
b = 33
if b > a:
     print("b is greater than a")
elif a == b:
    print("a and b are equal") #correct

#6
a = 200
b = 33
if b > a:
     print("b is greater than a")
elif a == b:
     print("a and b are equal")
else:
    print("a is greater than b") #correct

#5.Write a Python program to find those numbers which are divisible by 7 between 1 and 1000
for i in range (1,1000):
    if i % 7 == 0:
        print (i, "is divisible by 7")

#6.Write a Python program to find those numbers which are multiple of 5 between 1 and  1000
for i in range (1,1000):
    if i % 5 == 0:
        print (i, "is a multiple of 5")

#7.Write a Python program to count the number of even and odd numbers from a series of numbers  -  numlist = [1,2,3,4,5,6,7,8,9,10,11]
for i in range (1,11):
    if i % 2 == 0:
        print (i, "is an even number")

for i in range (1,11):
    if i % 2 == 1:
        print (i, "is an odd number")

#8.Write a python program to Reverse the following list using for loop -  numlist = [1,2,3,4,5,6,7,8,9,10,11]
numlist = [1,2,3,4,5,6,7,8,9,10,11]
numlist.reverse()
print(numlist)

#The End


