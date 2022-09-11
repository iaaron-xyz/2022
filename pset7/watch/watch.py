"""
Usage:
$ python watch.py

Description:
This program gets html code, parse the code and extract any youtube url
then converts that url to a shortened youtube url and returns it.

Examples:
$ python watch.py
HTML: <iframe width="560" height="315" src="https://www.youtube.com/embed/xC-j6vTqMxU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
https://youtu.be/xC-j6vTqMxU
"""
import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # extract the youtube url
    if url := re.search(r'src="(?:https?://)?(?:www\.)?youtube\.com/(?:embed/)?([\w-]+)"', s):
        # extract id video
        id = url.group(1)
        return f"https://youtu.be/{id}"

    return


if __name__ == "__main__":
    main()