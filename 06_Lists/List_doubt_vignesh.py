# cars = ['suzuki', 'tata', 'honda', 'ford']
# print(cars)
#
#
# print(type(cars))
# cars.extend(["cd"])
# cars.extend("cd")
# print(cars)
# print("====")
# letters = ["a", "b"]
# print(type(letters))
# letters.extend("cd")
# print("Letters list:", letters)

# list doubt sathya
import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
print(old_list)
new_list = copy.copy(old_list)
print(f"new_list before modification: {new_list}")
old_list.append("*****")
print(f"old_list after append: {old_list}")
print(f"new_list after appending: {new_list}")

print("modification 2 ")
old_list[1][0] = 99
print(f"old_list after append: {old_list}")
print(f"new_list after appending: {new_list}")

print("Old list:", old_list)
print("New list:", new_list)