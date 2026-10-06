counts = {}

user_input = input().split()

for name in user_input:
    counts[name] = counts.get(name, 0) + 1

for key, value in counts.items():
    print(key, value)
