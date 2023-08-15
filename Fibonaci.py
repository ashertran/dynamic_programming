n=100
f = [0]*n
f[0]=0
f[1]=1
print(f)
for i in range(2,n):
    print(i)
    f[i] = f[i-1] + f[i-2]

print(f)


