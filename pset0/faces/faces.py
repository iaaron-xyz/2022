"""
Usage: $ python3 face.py

Description:
The user gets a prompt to type a sad :( or happy face :)
the receives its equivalent emoji as output

Examples:
$ python3 faces.py 
:)
🙂
"""

text = input()
new_text = text.replace(":)","🙂").replace(":(","🙁")
print(f"{new_text}")