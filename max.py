n=int(input())
l=list(map(int,input().split()))
p=[]
for i in range(n):
	if l[i-1]>max(l[i:n]):
		p.append(l[i-1])
if l[-1] not in p:
	p.append(l[-1])
print(*p)
print(max(l))
