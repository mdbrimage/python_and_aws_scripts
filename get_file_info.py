"""
A script that extracts information such as the name and size about the 
files in the current working directory and stores it in a list of dictionaries.
"""

import os

#current_working_directory = os.getcwd() #Return a string representing the current working directory. Stores the value in the variable current_working_directory

fileList = [] #initializes an empty list to store the dictionaries containing file information. 

for file in os.listdir(): #Iterate through the list of files in the directory

    if os.path.isfile(file): #checking to validate that file is a regular file
    
        fileInfo = {
                'File Name': file, 'size': os.path.getsize(file) 
            }
            
        fileList.append(fileInfo)
        
print(fileList)

