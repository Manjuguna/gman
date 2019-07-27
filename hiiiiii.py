h1,u1=map(str,input().split())
yast=0
if len(h1)>len(u1):
  h1,u1=u1,h1
n1=0
while n1<len(h1):
  yast+=(ord(u1[n1])-ord(h1[n1]))
  n1+=1
for n1 in range(n1,len(u1)):
  yast+=ord(u1[n1])-ord('a')+1
print(yast)
