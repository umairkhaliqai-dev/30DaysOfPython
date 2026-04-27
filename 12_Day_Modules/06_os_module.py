# The os module lets you interact with your operating system — get directories, create folders, list files, and more.
import os

print(os.getcwd())           # current working directory
print(os.listdir('.'))       # list files in current dir
os.mkdir('test_folder')      # create a new folder
print(os.path.exists('test_folder'))  # → True so when i run this command i got new folder name test folder in my VS code explorer on the side bar 

# import the module
import os
# Creating a directory
os.mkdir('directory_name')
# Changing the current directory
os.chdir('path')
# Getting current working directory
os.getcwd()
# Removing directory
os.rmdir()