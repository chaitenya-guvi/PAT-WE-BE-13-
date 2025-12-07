"""
write mode - 'w'
overwrites the existing content
creates a new file if the specified file does not exist

writelines() - writes a list of strings to a file
write() - writes a single string to a file
writelines() does not add newline characters between the strings, so you need to include them if required.
"""

with open(file = './files/writing_file_example.txt',mode = 'w') as f:
    f.write('This text will be written in a newly created file')
    f.writelines(["\n Line 1","\n Line2","\n Line 3"])