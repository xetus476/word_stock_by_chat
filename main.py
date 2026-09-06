a, b = map(int, input().split())
sp = list(map(int, input().split()))
new_sp = []
for i in range(0, a-1):
    for j in range(i+1,a-1):
        c=sp[i]*sp[j]
        new_sp.append(c)
print(new_sp)