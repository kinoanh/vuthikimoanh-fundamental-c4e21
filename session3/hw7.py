sheeps = [5, 7, 300, 90, 24, 50, 75]
n=len(sheeps)
print (" my name is hiep , here is my flock:")
print(sheeps)
m=max(sheeps)
print("my biggest sheep", m , "let shear it")
a=sheeps.index(m)
sheeps[a]=8
print("after shearing")
print(sheeps)
for i in range(n):
    sheeps[i] += 50
print("One month has passed, now here is my flock")
print(sheeps)