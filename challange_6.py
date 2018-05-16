# MISSING

import urllib.request
import pickle

# http://www.pythonchallenge.com/pc/def/peak.html
url = "http://www.pythonchallenge.com/pc/def/banner.p"


def step_1():
    with urllib.request.urlopen(url) as res:
        r = res.read()
        pickle.dump(r, open("./inputs/challange_6.p", "wb"))


def step_2():
    p = pickle.load(open("./inputs/challange_6.p", "rb"))
    print(p)


if __name__ == '__main__':
    step_2()
