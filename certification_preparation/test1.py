num = int(input())
arr = list(map(int, input().split()))

print(max([int(n) for n in arr[:num]]))
