import urllib.request
import urllib.error
import re

# url changed because different placeholder of html text appears
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=53548"
while True:
    try:
        with urllib.request.urlopen(url) as res:
            html_content = res.read().decode("utf-8")
            node = re.search(r"[0-9]+", html_content)
            if node is None:
                break
            url = "http://www.pythonchallenge.com/pc/def/" + \
                  "linkedlist.php?nothing={}".format(node.group())
            print(url)
    except urllib.error.HTTPError as e:
        print(e)
