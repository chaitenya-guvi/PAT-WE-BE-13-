""" 1a2b3c """
import random
import string

def generate_random_string_chaitenya(length=6):
    characters = string.ascii_lowercase + string.digits
    print(''.join(random.choice(characters) for _ in range(length)))

#cretae a method and print someting inside it , call it from robot