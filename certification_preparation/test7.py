n = int(input())

converted = " ".join([str(n**2) for n in range(2, n + 1, 2)])
print(converted)
