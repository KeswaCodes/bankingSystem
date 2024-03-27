# import re

# pattern = re.compile(r"(\w+) (\w+)")
# matchObj = pattern.search("I am happy!")

# print("Group:", matchObj.group())
# print()
# first, second = matchObj.groups(2)
# print("Groups:", first, second)
# print()
# # print("Group2:", matchObj.group(2))
# # print()
# # print("Groups:",matchObj.groups(1))
# # print()
# print("Span:",matchObj.span())
# print()
# print("Start idx:",matchObj.start())
# print()
# print("End idx:",matchObj.end())

import re 

pattern = re.compile(r"(\$)?")
matchObj = pattern.search("$Money")

print(matchObj.group())

