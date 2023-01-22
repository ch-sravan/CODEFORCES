a,b=map(int,input().strip().split())
l=map(int,input().strip().split())
r=list(l)
c=0
for i in range(len(r)):
    if(r[i]>=r[b-1] and r[i]>0):
        c=c+1
print(c)
