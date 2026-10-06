"""
num = int(input())
arr = list(map(int, input().split()))

print(max([int(n) for n in arr[:num]]))
"""

"""
user_input = input()

count = 0

for alphabet in user_input:
    if alphabet == "a":
        count += 1

print(count)
"""

"""
user_range = int(input())

user_list = list(set(map(int, input().split())))

sliced_item = sorted(user_list, reverse=True)

print(sliced_item[1])
"""

"""
counts = {}

user_input = input().split()

for name in user_input:
    counts[name] = counts.get(name, 0) + 1

for key, value in counts.items():
    print(key, value)
"""

"""
n = int(input())

converted = " ".join([str(n**2) for n in range(2, n + 1, 2)])
print(converted)
"""

"""
students = {"Alice": 85, "Bob": 72, "Charlie": 91, "David": 68}

print(max(students, key=lambda x: students[x]))
"""

"""
text = "hello"

palindrome = True if text == text[::-1] else False

print(palindrome)
"""

n = int(input())

user_input = list(map(int, input().split()))

for num in user_input[:n]:
    if user_input.count(num) == 1:
        print(num)
        break
else:
    print(-1)


