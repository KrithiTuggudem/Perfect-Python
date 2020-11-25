a = 21
b = 10
c = 0

c = a + b
print ("Line 1 - Value of c is ", c)

#c = c + a
c += a
print ("Line 2 - Value of c is ", c)

#c = c * a
c *= a
print ("Line 3 - Value of c is ", c)

#c = c/a
c /= a
print ("Line 4 - Value of c is ", c)


c = 2

#c = c % 2
c %= a
print ("Line 5 - Value of c is ", c)

#c = c ** a
c **= a
print ("Line 6 - Value of c is ", c)

#c = c//a
c //= a
print ("Line 7 - Value of c is ", c)

#============================

a = 21
b = 10

#b = b * a
#c = b-a
b *=a
c = b - a
print ("Line 1 - Value of c is ", c)

a = 12
b = 10

#b = b + a
#a = a + b
#c = a + b
b +=a
a +=b
c = a + b
print ("Line 1 - Value of c is ", c)



#============================


a = 7
Total = 21

#Total = a + Total
Total += a # Using += Operator
print("The Value of the Total after using += Operator is: ", Total)

#Total = Total - a
Total -= a # Using -= Operator
print("The Value of the Total after using -= Operator is: ", Total)

#Total = Total * a
Total *= a # Using *= Operator
print("The Value of the Total after using *= Operator is: ", Total)

#Total = Total//a
Total //= a # Using //= Operator
print("The Value of the Total after using //= Operator is: ", Total)

#Total = Total//a
Total **= a # Using **= Operator
print("The Value of the Total after using **= Operator is: ", Total)

#Total + Total ** a
Total /= a # Using /= Operator
print("The Value of the Total after using /= Operator is: ", Total)

#Total = Total % a
Total %= a # Using %= Operator
print("The Value of the Total after using %= Operator is: ", Total)