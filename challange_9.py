#username = huge
#password = file

import sys
import urllib.request
from html.parser import HTMLParser

from PIL import Image, ImageDraw

url = "http://www.pythonchallenge.com/pc/return/good.html"

p = urllib.request.HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, "huge", "file")

auth_handler = urllib.request.HTTPBasicAuthHandler(p)
opener = urllib.request.build_opener(auth_handler)

urllib.request.install_opener(opener)


class MyParser(HTMLParser):

    def handle_comment(self, data):

        pos_first = int(data.find("first:"))
        pos_second = int(data.find("second:"))

        if pos_first == -1:
            return
        first_arr = data[pos_first + len("first:"):pos_second].split(",")
        first_arr = [int(i.replace("\n", "")) for i in first_arr]

        second_arr = data[pos_second + len("second:"):].split(",")
        second_arr = [int(i.replace("\n", "")) for i in second_arr]

        together = []
        for i in range(len(second_arr)):
            together.append((first_arr[i], second_arr[i]))

        im = Image.open("./inputs/good.jpg")

        draw = ImageDraw.Draw(im)
        draw.polygon(first_arr, fill=128)
        draw.polygon(second_arr, fill=128)

        del draw

        # write to stdout
        im.save("./inputs/good.png", "PNG")  # Solution: cow


with urllib.request.urlopen(url) as res:
    r = res.read().decode("utf-8")

    parser = MyParser()
    parser.feed(r)
