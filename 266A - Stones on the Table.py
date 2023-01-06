LINK:https://codeforces.com/problemset/problem/266/A

n=int(input())
l=list(input())
s=set(l)
if(len(s)==1):
    print(n-1)
else:
    c=0
    for i in range(n-1):
        if(l[i]==l[i+1]):
            c+=1
    print(c)
