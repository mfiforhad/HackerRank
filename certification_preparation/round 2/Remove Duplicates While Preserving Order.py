user_input = int(input())
arr = list(map(int, input().split()))

n = {}.fromkeys(arr[:user_input], 0)
modified = " ".join([str(k) for k in n])

print(modified)
