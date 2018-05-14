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

    for match in matches:
        print(match[4:5])

# http://www.pythonchallenge.com/pc/def/linkedlist.html
