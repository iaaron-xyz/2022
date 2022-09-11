"""
Usage:
$ pytest test_response.py

Description:
This program tests the email_validator(email) function in the
response.py file.
"""
from response import email_validator


def test_email_validator():
    assert email_validator("malan") == "Invalid"
    assert email_validator("malan at harvard dot com") == "Invalid"
    assert email_validator("malan@harvard.edu") == "Valid"
    assert email_validator("iaaron.xyz@gmail.com") == "Valid"
    assert email_validator("aaron@@gmail.com") == "Invalid"