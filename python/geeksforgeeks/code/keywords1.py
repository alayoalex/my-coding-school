# Python code to demonstrate  
# True, False, None, and, or , not 
  
# showing that None is not equal to 0 
# prints False as its false. 
print (None == 0) 
  
# showing objective of None 
# two None value equated to None 
# here x and y both are null 
# hence true 
x = None
y = None
print (x == y) 
  
# showing logical operation  
# or (returns True) 
print (True or False) 
  
# showing logical operation  
# and (returns False) 
print (False and True) 
  
# showing logical operation  
# not (returns False) 
print (not True) 

# Python code to demonstrate  
# del and assert 
  
# initialising list  
a = [1, 2, 3] 
  
# printing list before deleting any value 
print ("The list before deleting any value") 
print (a) 
  
# using del to delete 2nd element of list 
del a[1] 
  
# printing list after deleting 2nd element 
print ("The list after deleting 2nd element") 
print (a) 
  
# demonstrating use of assert 
# prints AssertionError 
# uncomment following line to see
# assert 5 < 3, "5 is not smaller than 3"