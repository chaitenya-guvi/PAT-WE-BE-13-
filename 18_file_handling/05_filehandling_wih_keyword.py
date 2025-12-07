"""
with keyword is a context manager
 that automatically handles opening and closing files.
When you use the with statement to open a file,
 it ensures that the file is properly closed after its suite finishes,
even if an exception is raised. This helps prevent resource leaks and makes the code cleaner and more readable.



"""

with open('./files/reading_file_example.txt') as f:
    lines = f.readlines()
    print(type(lines))
    print(lines)