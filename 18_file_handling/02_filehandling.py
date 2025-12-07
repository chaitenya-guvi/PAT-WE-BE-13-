f = open('./files/reading_file_example.txt')
txt = f.read()
print(type(txt))
print(txt)
print("111111!!!!!!!!!!!!"* 3)

txt2 = f.read()
print(f"text2 is :: {txt2} :: ")
f.close()




