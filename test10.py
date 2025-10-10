user_list = [(422161988, 'Илья', 'kabuntat')]
for user_tuple in user_list:
    user = tuple(map(str, user_tuple))
    print(user)
    print("    ".join(user))
