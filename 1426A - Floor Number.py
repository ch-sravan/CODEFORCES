LINK:https://codeforces.com/problemset/problem/1426/A

t=int(input())
for i in range(t):
    l=[]
    n,a=map(int,input().strip().split())
    if(n==1 or n==2):
        print("1")
    else:
        i=0
        b=2
        while True:
            if(n>b):
                b+=a
                i+=1
            else:
                break
        print(i+1)
