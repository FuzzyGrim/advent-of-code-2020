with open("input.txt") as file:
    data = file.read().splitlines()
print(data)

for i in range(0, len(data)):
    for j in range(i + 1, len(data)):
        if int(data[i]) + int(data[j]) == 2020:
            print(int(data[i]) * int(data[j]))


for i in range(0, len(data)):
    for j in range(i + 1, len(data)):
        for k in range(j + 1, len(data)):
            if int(data[i]) + int(data[j]) + int(data[k]) == 2020:
                print(int(data[i]) * int(data[j]) * int(data[k]))
