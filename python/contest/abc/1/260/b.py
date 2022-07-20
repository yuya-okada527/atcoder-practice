n, x, y, z = map(int, input().split())
A = map(int, input().split())
B = map(int, input().split())

students = []
for i, (a, b) in enumerate(zip(A, B), start=1):
    students.append((a * 10**9 + b * 10**6 + (a + b) * 10**3 + (1000 - i), i))

for student in sorted(sorted(students, key=lambda x: x[0], reverse=True)[:x+y+z], key=lambda x: x[1]):
    print(student[1])
