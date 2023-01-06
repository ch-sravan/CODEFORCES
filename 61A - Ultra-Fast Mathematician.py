LINK:https://codeforces.com/contest/61/problem/A

l1=list(input())
l2=list(input())
l3=[]
h1=0
h2=0
i=0
while True:
    if((l1[h1]=='1' and l2[h2]=='1')or(l1[h1]=='0' and l2[h2]=='0')):
        l3.append("0")
    else:
        l3.append("1")
    i+=1
    h1+=1
    h2+=1
    if(i==len(l1)):
        break
r="".join(l3)
print(r)
