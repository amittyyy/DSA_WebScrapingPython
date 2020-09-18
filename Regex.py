import re

message = "Call me on 641-451-3464 or also you can call me on my home number (631) 590-9522"
pipeMessage = 'Batman Lost his temper while ridding BatMobile'

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')   # \d for digit.
phoneNumberRegexByGroup = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')  # Can get area code and other part separately
phoneNumberRegexAreaCode = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
phoneNumberRegAreaOptional = re.compile(r'(\d\d\d-)? \d\d\d-\d\d\d\d')

pipeRegex = re.compile(r'Bat(man|mobile|copter|bat|Boose)')
matchRegex = re.compile(r'Bat(wo)?man')

anythingRegex = re.compile(r'.at')

matchedObjects = phoneNumberRegex.search(message)
print(matchedObjects.group())    # this will give you actual value.
print(phoneNumberRegex.findall(message))  # This is give you all matching values

#Area Codes
matchedObjectsG = phoneNumberRegexByGroup.search(message)
print(matchedObjectsG.group(1))   # result will be area code 641

#Bracket Patter Phone Number

matchedObjectsG = phoneNumberRegexAreaCode.search(message)
print(matchedObjectsG.group())

#PipeLine Regex
pipeRegexObj = pipeRegex.search(pipeMessage)
print(pipeRegexObj.group())
print(pipeRegex.findall(pipeMessage))

#Match Regex
matchRegexObj = matchRegex.search("The Advanture of Batman")
print(matchRegexObj.group())

#anything
anythingRegexObj = anythingRegex.search("The cat in the hat sat on the flat mat.")
print(anythingRegexObj.group())
print(anythingRegex.findall("The cat in the hat sat on the flat mat."))
