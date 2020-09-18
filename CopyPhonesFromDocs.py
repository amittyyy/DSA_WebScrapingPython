#Todo: Import
import re
import pyperclip

#Todo: Creeate Regex for phone, Email
phoneRegex = re.compile(r'''
# 444-455-4545, 444-4444, (455) 555-5555, 555-0000 ext 12345, ext. 12345, x12345 
(
((\d\d\d) | (\(\d\d\d\)))? # Area Code (optional)
(\s|-) # first separator
\d\d\d    # first 3 digits
-   # Separator
\d\d\d\d   # Last 4 Digits 
(((ext(\.)?\s) |x)   # Extension Word part(Optional)
(\d{2,5}))?    # Extension Number part(Optional)
)
''', re.VERBOSE)
#Todo:- get the text from the clipboard
emailRegex = re.compile(r'''
#Some .+-thing@(\d{2,5})?.com
[a-zA-Z0-9_.+]+    # Name Part
@   # @symbol
[a-zA-Z0-9_.+]+     #domain Name part
''', re.VERBOSE)
#Todo:  Extract the email and phone number
text = pyperclip.paste()
#Todo: Copy the extracted email and phone number to the clipboard

extractedPhones = phoneRegex.findall(text)
allPhones = []
for phoneNumber in extractedPhones:
    allPhones.append(phoneNumber[0])

extractEmails = emailRegex.findall(text)

result = '\n'.join(allPhones) + '\n' + '\n'.join(extractEmails)    # Show Phone number / Emails in the list
pyperclip.copy(result)
print(result)
print(extractEmails)