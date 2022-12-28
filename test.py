import random
n = int(input('inter n='))
a1 = [int(i) for i in range(n, 0, -1)]
a2 = [random.randint(0, 100) for i in range(n+1)]
print(a1)
print(a2)
print(a2[-1])
