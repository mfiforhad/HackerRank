s = "programminG"

count = {}

for alphabet in s:
    count[alphabet] = count.get(alphabet, 0) + 1

higest = max(count, key=lambda x: count[x])

print(higest)
