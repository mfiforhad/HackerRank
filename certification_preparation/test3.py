user_range = int(input())

user_list = list(set(map(int, input().split())))

sliced_item = sorted(user_list, reverse=True)

print(sliced_item[1])
