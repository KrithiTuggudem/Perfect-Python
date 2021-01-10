#1. 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

#1.1 Print fourth, and fifth item from the list
print(thislist[4:6])
#1.3 print items from the beginning to, but NOT including, "melon"
print(thislist[ :5])
#1.3 print item from "banana" to the end
print(thislist[1: ])


#2. 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

#2.1 Change/replace  the value of  "banana" to "orange" in the list.
thislist[1] = "orange"
print (thislist)
#2.2 Change the values "cherry" and   "orange" with the values "blackcurrant" and "watermelon"
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[2:4] = ["blackcurrant, watermelon"]
print(thislist)
#2.3 Change the third and fourth value by replacing it with "mango"
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[3:5] = ["mango"]
print(thislist)


#3. 
thislist = ["apple", "banana", "cherry"]

#3.1 use function to insert "watermelon" as the third item
thislist.insert(2, "Watermelon")
print(thislist)
#3.2 use function to insert "watermelon" as the Last item
thislist = ["apple", "banana", "cherry"]
thislist.insert(3,"watermelon")
print(thislist)
#3.3 use function to insert "watermelon" as the first item
thislist = ["apple", "banana", "cherry"]
thislist.insert(0,"watermelon")
print(thislist)


#4. 
thislist = ["apple", "banana", "cherry"]

#4.1 use function to append "watermelon" to list.
thislist.append("watermelon")
print(thislist)


#5. What is the difference between insert and append function? show with example?

#The insert function is able to insert anything anywhere, even the end:
thislist = ["apple", "banana", "cherry"]

thislist.insert(2, "grape")
thislist.insert(3, "orange")
print(thislist)

#The append function only inserts at the end. This is because append only takes 1 argument
thislist = ["apple", "banana", "cherry"]

thislist.append("grape")
thislist.append("orange")
print(thislist)

#END OF ASSIGHNMENT