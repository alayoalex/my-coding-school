# using "in" to check  
if 's' in 'geeksforgeeks': 
       print ("s is part of geeksforgeeks") 
else : print ("s is not part of geeksforgeeks") 
  
# using "in" to loop through 
for i in 'geeksforgeeks': 
    print (i,end=" ") 
  
print ("\r") 
      
# using is to check object identity 
# string is immutable( cannot be changed once alloted) 
# hence occupy same memory location 
print (' ' is ' ') 
  
# using is to check object identity 
# dictionary is mutable( can be changed once alloted) 
# hence occupy different memory location 
print ({} is {}) 

# Python code to demonstrate working of 
# global and non local 
  
#initializing variable globally 
a = 10
  
# used to read the variable 
def read(): 
    print (a) 
  
# changing the value of globally defined variable 
def mod1(): 
    global a  
    a = 5
  
# changing value of only local variable 
def mod2(): 
    a = 15
  
# reading initial value of a 
# prints 10 
read() 
  
# calling mod 1 function to modify value 
# modifies value of global a to 5 
mod1() 
  
# reading modified value 
# prints 5 
read() 
  
# calling mod 2 function to modify value 
# modifies value of local a to 15, doesn't effect global value 
mod2() 
  
# reading modified value 
# again prints 5 
read() 
  
# demonstrating non local  
# inner loop changing the value of outer a 
# prints 10 
print ("Value of a using nonlocal is : ",end="") 
def outer(): 
    a = 5
    def inner(): 
        nonlocal a  
        a = 10
    inner() 
    print (a) 
  
outer() 
  
# demonstrating without non local  
# inner loop not changing the value of outer a 
# prints 5 
print ("Value of a without using nonlocal is : ",end="") 
def outer(): 
    a = 5
    def inner(): 
        a = 10
    inner() 
    print (a) 
  
outer() 