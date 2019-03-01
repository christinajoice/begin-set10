n=int(input("Enter number of natural numbers"))
li=[]
for i in range(0,n):
  li.append(input())
str=" "
str.join(li)
for i in str:
  if str[i+1]!=str[i]+1:
    print(i)
