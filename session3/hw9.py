sheeps = [5, 7, 300, 90, 24, 50, 75]
n = len(sheeps)

print("Hello, my name is Quinn and these are my ship sizes")
print(sheeps)

for j in range(1,4):
    print("MONTH", j)
    for i in range(n):
        sheeps[i] += 50
        print("One month has passed, now here is my flock")
        print(sheeps)
    
    m=max(sheeps)
    print("my biggest sheep", m , "let shear it")
    a=sheeps.index(m)
    sheeps[a]=8
    print("after shearing")
    print(sheeps)