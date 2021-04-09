# coding   : utf-8 
# @Time    : 21/04/05 10:07
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 1.py
# @Software: PyCharm


# T=int(input())
# T = 3
# value=[]
# for i in range(T):
#     v=list(map(int,input().split( )))
#     value.append(v)
value = [[1,100,15],[1,1,15]]
for v in value:
    s=0
    while v[0]<=v[1]:
        s=s+pow(v[0]+10**(-v[2]),1/3)-pow(v[0],1/3)
        v[0]+=1
    print('%.5e'%s)

for l,r,k in value:
    s=0
    while l<=r:
        s=s+pow(l+10**(-k),1/3)-pow(l,1/3)
        l+=1
    print('%.5e'%s)

def func(l,r,k):
    res = 0
    while l <= r:
        res +=