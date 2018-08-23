sheeps = [5, 7, 300, 90, 24, 50, 75]
s = len(sheeps)
print(sheeps)

for j in range(4):
    print("month", j+1)
    for i in range(s):
        sheeps[i] += 50
        print(sheeps)