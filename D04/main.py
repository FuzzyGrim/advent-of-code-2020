with open("input2.txt") as file:
    data = file.read().splitlines()
print(data)

fixed_list = []

for i in range(0, len(data)):
    fixed_list.append([])
print(fixed_list)

i = 0
j = 0

while i < len(data):
    if data[i] == "":
        j += 1
    else:
        fixed_list[j].append(data[i])
        print(fixed_list)

    i += 1
for i in range(0, len(fixed_list)):
    if fixed_list[i] == []:
        k = i
del fixed_list[k:]
print(fixed_list)
print(len(fixed_list))

