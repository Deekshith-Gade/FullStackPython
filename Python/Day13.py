n = int(input("Enter n value: "))

original = n
rev = 0

while n > 0:
    r = n % 10
    rev = rev * 10 + r
    n = n // 10

print(f"The reverse of {original} is:", rev)

n = int(input("Enter Input:"))

s = str(n)

c = 0

for i in s:
    if int(i) % 2 == 0:
        c = c + 1

print("Count of even digits:", c)

n=int(input("Enter Number"))
s=str(n)
for i in range(0,len(s),2):
    print(s[i] ,end="")
    

n=int(input("Enter Number"))
s=str(n)
for i in range(len(s)-1,-1,-2):
    print(s[i] ,end="")

n=int(input("Enter Number"))
s=str(n)
a=0
if len(s)%2==0:
    print('Invaild Input')
else:
    a=len(s)//2
    print(s[a])
    