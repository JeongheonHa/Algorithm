n = int(input())
students = []
for _ in range(n):
    data = input().split()
    students.append(data)
    
students.sort(key = lambda x: x[1])

for student in students:
    print(student[0], end = " ")