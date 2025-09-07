# type conversion
# implicit type conversion

integer_number = 123
print(type(integer_number))
float_number = 1.23
print(type(float_number))
new_number = integer_number + float_number


# display new value and resulting data type
print("Value:",new_number)
print("Data Type:",type(new_number))
#
#
print('*******************')
num_string = '12'
num_integer = 23

print(type(num_string))
print(type(num_integer))
#
#

print("Data type of num_string before Type Casting:",type(num_string))
# # explicit type conversion
num_string = int(num_string)

#
print("Data type of num_string after Type Casting:",type(num_string))


num_sum = num_integer + num_string


print("Sum:",num_sum)
print("Data type of num_sum:",type(num_sum))
