with open("input.txt") as file:
    data = file.read().split('\n')



position = 3
count = 0

for row in data[1:(len(data) - 1)]:
    if row[position] == "#":
        count += 1
    position += 3
    if position > len(data[0]) - 1:
        position -= len(data[0])

print(count)




rights = [1, 3, 5, 7, 1]
downs = [1, 1, 1, 1, 2]
count_p2 = 1
for i, j in zip(rights, downs):
    i_temp = i
    current_count = 0
    for row in data[j:(len(data) - 1):j]:
        if row[i] == "#":
            current_count += 1

        i += i_temp
        if i > len(data[0]) - 1:
            i -= len(data[0])
    count_p2 *= current_count

print(count_p2)

