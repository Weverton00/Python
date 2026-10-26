# Finding Phone Numbers
import re


def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(3):
        if not text[i].isdecimal():
            return False
    if text[3] != "-":
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != "-":
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

message: string = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office."

for i in range(len(message)):
    chunk = message[i:i + 12]
    if isPhoneNumber(chunk):
        print(f"Phone number was found {chunk}")
print("Scan finalizado.")

#Usando uma regEx - regular expression

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search("My phone number is 415-555-4242.")
print("Phone number was found:" + mo.group())
