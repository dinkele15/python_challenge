import re

matches = []
with open("./inputs/challange_4.txt", "r") as f:
    matches = re.findall("[^A-Z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[^A-Z]{1}",
                         f.read())

    """
    qIQNlQSLi
    eOEKiVEYj
    aZADnMCZq
    bZUTkLYNg
    uCNDeHSBj
    kOIXdKBFh
    dXJVlGZVm
    gZAGiLQZx
    vCJAsACFl
    qKWGtIDCj
    """

    print("".join([match[4:5] for match in matches]))

# http://www.pythonchallenge.com/pc/def/linkedlist.html
