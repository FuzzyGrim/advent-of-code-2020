with open("input.txt") as file:
    data = file.read().split('\n')



valid = 0

for i in range(0, len(data) - 1):
   strings = data[i].split()
   policy = strings[0].split("-")
   letter = strings[1][0]
   count = strings[2].count(letter)
   if count >= int(policy[0]) and count <= int(policy[1]):
       valid += 1

print(valid)




valid = 0

for i in range(0, len(data) - 1):
   strings = data[i].split()
   policy = strings[0].split("-")
   letter = strings[1][0]
   if not(strings[2][int(policy[0]) - 1] == letter and strings[2][int(policy[1]) - 1] == letter):
       if strings[2][int(policy[0]) - 1] == letter or strings[2][int(policy[1]) - 1] == letter:
           valid += 1

print(valid)
