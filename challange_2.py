# find rare characters in the mess below:

with open("./inputs/challange_3.txt", "r") as f:

    frequency_list = {}

    for symbol in f.read():
        frequency_list[symbol] = 1 if frequency_list.get(
            symbol) is None else frequency_list[symbol] + 1

    print("".join([c for c, v in frequency_list.items() if v < 10]))

# http://www.pythonchallenge.com/pc/def/equality.html
