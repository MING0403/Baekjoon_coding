n = int(input())
users = []

for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    users.append((age, name))

users.sort(key = lambda age: (age[0]))

for i in users:
    print(i[0], i[1])