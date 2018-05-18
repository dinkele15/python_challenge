# len(a[30]) ?
a = [1, 11, 21, 1211, 111221]

next_number = str(a[len(a) - 1])

conc = ""

for i in range(len(next_number)):
    if i + 1 >= len(next_number):
        break
    if next_number[i] == next_number[i + 1]:
        conc += next_number[i]
    else:
        conc += "," + next_number[i]

print(conc)
