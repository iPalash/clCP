import sys
int_min=-sys.maxsize
n,k=map(int,input().split())
a=[0]+list(map(int,input().split()))
dp=[-1]*(n+1)
visited=[-1]*(n+1)
for i in range(n+1):
    dp[i]=[int_min]*2
    visited[i]=[False]*2
def rec(curr,dir):
    # print('Visiting:',curr,dir)
    if curr==1 and dir==0:
        return 0
    if visited[curr][dir]:
        return dp[curr][dir]
    visited[curr][dir]=True
    res=int_min
    if (dir):
        if curr+1<=n:
            res=max(res, a[curr+1]+rec(curr+1,1))
        if curr+2<=n:
            res=max(res, a[curr+2]+rec(curr+2,1))
        if curr-1>0:
            res=max(res, a[curr-1]+rec(curr-1,0))
        if curr-2>0:
            res=max(res, a[curr-2]+rec(curr-2,0))
    else:
        if curr-1>0:
            res=max(res, a[curr-1]+rec(curr-1,0))
        if curr-2>0:
            res=max(res, a[curr-2]+rec(curr-2,0))
    # print('Visited:',curr,dir)
    dp[curr][dir]=res
    return res
print(max(rec(k,1),rec(k,0)))
