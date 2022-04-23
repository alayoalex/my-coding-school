"""Every program that runs on your computer has a current working directory, or cwd. 
Any filenames or paths that do not begin with the root folder are assumed to be under 
the current working directory. You can get the current working directory as a string 
value with the os.getcwd() function and change it with os.chdir().
"""

import os
print(os.getcwd())
#os.chdir('C:\\Windows\\System32')
#print(os.getcwd())
os.makedirs(os.path.join(os.getcwd(), 'delicious', 'walnut'))
