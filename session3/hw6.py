sheeps = [5, 7, 300, 90, 24, 50, 75]
print(sheeps)
m = max(sheeps)
print("biggest sheep : ", m)

a=sheeps.index(m)
sheeps[a] = 8

print(sheeps)