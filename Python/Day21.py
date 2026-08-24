path="/Users/deekshithgade/Documents/new.txt"

file=open(path,"w")
file.write("Hello World!")
file.close()
print("file written successfully")

file=open(path,"r+")
print(file.read())
file.seek(0)
file.write("Hi this is Deekshith\n")
print(file.read())
file.close()

l=["Line1\n","Line2\n","Line3\n"]
file=open(path,"a")
file.writelines(l)
file.close()

file=open(path,"r")
print(file.read())
file.close()


