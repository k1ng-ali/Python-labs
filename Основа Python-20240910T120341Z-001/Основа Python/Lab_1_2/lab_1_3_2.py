n = int(input("Введите количество строк: "))
login_data = {}
for i in range(n):
    line = input().split()
    login = line[0]
    date = line[1]
    ip = line[2]
    key = date + '_' + login
    if key in login_data:
        login_data[key].append(ip)
    else:
        login_data[key] = [ip]
max_login = None
max_count = 0
for key in login_data:
    count = len(set(login_data[key]))
    if count > max_count:
        max_count = count
        max_login = key.split('_')[1]
print("Логин с максимальным количеством различных IP адресов: ", max_login)

