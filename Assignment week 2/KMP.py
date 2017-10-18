import re

sentence = input("Insert Name Here")

result = re.findall("[A-Z]",sentence)
print (result)