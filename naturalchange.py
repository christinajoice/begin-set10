n=int(input("Enter number of natural numbers"))
li=[]
for i in range(0,n):
  li.append(input())
for i in range(0,len(li)):
  if li[i+1]!=li[1]+1:
    print(i)
