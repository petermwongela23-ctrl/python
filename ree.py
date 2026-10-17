import re
text="The rain in Spain"
x=re.search("^The.*Spain$",text)
if x:
    print("Yes we have a match")
else:
    print("No match!")