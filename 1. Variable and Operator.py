#In this chapter, we'll learn:
#   Variables
#   Basic operators

#Variable is the memory space that has name and value.
#The value can change.


#You can declare variables like it:
a = 10
#It means that put '10' in a.
#This statement is called assignment.

#You can also change the value of variables.
a=15
#Now a has changed to 15.

#Or you can use operator to change the value.
a = a + 1
#Now the value of the variable a has increased by 1.

#This has the same meaning.
a += 1

#If you want to decrease the value by 1:
a -= 1 #same as 'a = a-1'

a *= 2 #same as 'a= a*2' (In python, * means multiply)

a /= 2 #same as 'a = a/2' (In python / means division)

#Other than those, **= (exponentiating), //= (return the integer of value of division), %= (return the rest of division)



#There are some rules when you name variables.
#1. Don't put space in the name.
#For example, The statement 'my age = 20' causes error.
#So if you want to divide the words in variables, put _ instead of space.

#2. Start with letter or _.
#These names are available : a, a123, my_name, MyName, _private, __s

#3. Don't use special character like !, @, #, $, %.
#4. Reserved words(ex. print, for, import etc.) are not available in variables' names.

#You can use the value by using the name.
print(a) #print 16, the value of a.

#You can use variables when you want to get an input from user or you use same value several times.