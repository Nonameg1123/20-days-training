l=int(input())
r=int(input())
print(int((r/7)-(l/7)))
c=0
for i in range(l,r+1):
    if i%7==0:
        c+=1
print(c)