#!/usr/bin/python3
# Practice writing some expressions and conversions yourself.
# In this scenario, we have a directory with 5 files in it.  
# Each file has a different size: 2048, 4357, 97658, 125, and 8.
# Fill in the blanks to calculate the average file size by having Python add all the values for you, and then set the files variable to the number of files. Finally, output a message saying "The average size is: " followed by the resulting number. 
total = 2048 + 4357 + 97658  + 125 + 8
files = 5
average = total / files
print("The average size is: " + str(average))