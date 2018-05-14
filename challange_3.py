# find rare characters in the mess below:

all_symbols = set()

with open("./inputs/challange_3.txt", "r") as f:
    for symbol in f.read():
        all_symbols.add(symbol)
    frequency_list = {x: 0 for x in all_symbols}
    f.seek(0)
    for symbol in f.read():
        frequency_list[symbol] += 1
    print(frequency_list)

# i y a l t u e q -> equality
# http://www.pythonchallenge.com/pc/def/equality.html
