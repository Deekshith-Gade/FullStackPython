import re
s=input("enter patter to check:")
m=re.match(s,"abaaab")
if m!=None:
    print("match is available:")
    print(m.start(),m.end())
else:
    print("not available!")



m=re.fullmatch(s,"abaaabab")
if m!=None:
    print("pattern is same as target string")
    print(m.start(),m.end())
else:
    print("not available!")


pattern=r'^[0-9 a-z A-Z._%+-]+@gmail\.com$'
emails=['deekshitgade123@gmail.com','deekshith.gade3112@gmail.com','deekshithgade3@gmail.com']
for email in emails:
    if re.match(pattern,email):
        print(f"{email} is valid gmail address:")
    else:
        print(f"{email} is not valid")


text="phone:122-123-199"
m=re.sub(r'\d','#',text)
print(m)


text = "apple,banana;orange-grape"
result = re.split(r'\W+', text)
print(result)

