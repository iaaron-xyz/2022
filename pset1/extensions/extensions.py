"""
USAGE:
$ python3 extensions.py

DESCRIPTION:
implement a program that prompts the user for the name of a file and then
outputs that file's media type if the file's name ends, case-insensitively,
in any of these suffixes:
.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
If the file's name ends with some other suffix or has no suffix at all,
output application/octet-stream instead, which is a common default.

EXAMPLES:
$ python3 extensions.py
File name: zip
application/zip

$ python3 extensions.py
File name: jpeg
image/jpeg

MIME types obtained from: https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types
"""

# Receive the file name from the user
file_name = input("File name: ")

# get the extension
dot = file_name.find(".")
ext = file_name[dot+1:].lower().replace(" ","")

# Check if the extension fits with some media type
#media_type = "application/octet-stream"
if ext == "gif":
    print("image/gif")
elif ext=="jpg" or ext=="jpeg":
    print("image/jpeg")
elif ext == "png":
    print("image/png")
elif ext == "pdf":
    print("application/pdf")
elif ext == "txt":
    print("text/plain")
elif ext == "zip":
    print("application/zip")
else:
    print("application/octet-stream")
