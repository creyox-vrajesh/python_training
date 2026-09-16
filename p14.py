# Write a Python program that uses Regular Expressions (re) to extract a specific block of text enclosed within a <div class="predefined"> and its closing </div> tag from a block of HTML code.

import re

html_file = open('./extra/demo.html', 'r')
content =  html_file.read()

text = "<div class=\"predefined\"> Hello, welcome to creyox </div>"
pattern = '<div class="predefined">(.*)</div>'
# print(pattern)

# result = pattern in content
result = re.findall(pattern, content, re.DOTALL)
# result = re.search(pattern, text)

print(result[0].strip())
# print(result.group())