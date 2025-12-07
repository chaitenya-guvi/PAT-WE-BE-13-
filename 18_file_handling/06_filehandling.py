"""
append mode - 'a'

adds to the end of the file
without deleting the existing content
"""

with open(file='./files/reading_file_example.txt',mode='a') as f:
    f.write('\n Line 3 This text has to be appended at the end')