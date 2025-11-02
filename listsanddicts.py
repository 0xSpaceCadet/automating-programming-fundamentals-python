c_name=[]
max_len = 3

while len(c_name)<max_len:
    istream = input("Please enter your name: (or ENTER to quit storing): ")
    if istream == '':
        break
    c_name.append(istream)

print(c_name)
a, b, c = c_name
print(a, b, c)
print()


for index, item in enumerate(c_name):
    print(index, item)


