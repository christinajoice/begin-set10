n=int(input())
li=list(map(int,input().split()))
for i in range(len(li)):
  if li[i+1]!=li[i]+1:
    break
print(i+1)
