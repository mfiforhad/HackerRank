s = "programminG"

count = {}

for alphabet in s:
    count[alphabet] = count.get(alphabet, 0) + 1

higest = max(count, key=lambda x: count[x])

print(higest)

# max alternative

max_key = ""
max_value = 0

for key, value in count.items():
    if value > max_value:
        max_key = key
        max_value = value

print(max_key)
