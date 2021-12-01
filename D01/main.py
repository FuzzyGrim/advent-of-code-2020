with open("input.txt") as file:
    data = file.read().split('\n')

for i in range(0, len(data) - 1):
    for j in range(i + 1, len(data) - 1):
        if int(data[i]) + int(data[j]) == 2020:
            print(int(data[i]) * int(data[j]))


for i in range(0, len(data) - 1):
    for j in range(i + 1, len(data) - 1):
        for k in range(j + 1, len(data) - 1):
            if int(data[i]) + int(data[j]) + int(data[k]) == 2020:
                print(int(data[i]) * int(data[j]) * int(data[k]))
