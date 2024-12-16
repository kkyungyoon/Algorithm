N = int(input())
person_list = []
for _ in range(N):
    age, name = input().split()
    age = int(age)
    person_list.append([age, name])
person_list.sort(key= lambda x: (x[0]))

for person in person_list:
    print(*person)