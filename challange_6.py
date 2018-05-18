import zipfile  # start from 90052.txt
import re

all_files = []


def main():
    start_file = "90052.txt"
    with zipfile.ZipFile("./inputs/channel.zip") as myzip:
        all_comments = []
        while True:
            content = myzip.read(start_file).decode("utf-8")
            if "Next nothing is " not in content:
                break
            f = re.search("[0-9]+$", content).group()
            all_comments.append(myzip.getinfo(
                f + ".txt").comment.decode("utf-8"))
            start_file = f + ".txt"
        print("".join(all_comments))


if __name__ == '__main__':
    main()
    # It's in the air. Look at the letters (oxygen)
