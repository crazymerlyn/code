n = int(input())

users = {}
logged_in = set()

for _ in range(n):
    com = input().split()
    if com[0] == 'register':
        if com[1] in users:
            print('fail: user already exists')
        else:
            users[com[1]] = com[2]
            print('success: new user added')
    elif com[0] == 'login':
        if com[1] not in users:
            print('fail: no such user')
        elif com[2] != users[com[1]]:
            print('fail: incorrect password')
        elif com[1] in logged_in:
            print('fail: already logged in')
        else:
            logged_in.add(com[1])
            print('success: user logged in')
    else:
        if com[1] not in users:
            print('fail: no such user')
        elif com[1] not in logged_in:
            print('fail: already logged out')
        else:
            logged_in.remove(com[1])
            print('success: user logged out')
