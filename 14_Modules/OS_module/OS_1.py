import os
from os import getcwd

"""
chdir -ch dir 
mkdir - makin new folder 
listdir - listing all files in a directory
getcwd - get current working directory 
rmdir - remove directory 
rename - rename takes 2 arguments (old name, new name) 
"""

print(os.getcwd())  # get current working directory
os.mkdir("example_directory_chaitenya")

print(getcwd())

print(os.listdir())

os.rename("example_directory_chaitenya","example_directory_PAT")

print(os.listdir())