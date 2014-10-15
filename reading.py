f = open("scores.txt", "r")

students ={}

for line in f:
    entry = line.strip().split(",")
    student = entry[0]
    grade = entry[1]
    students[student] = grade
    print (student + ":" + grade)

print()
print (students)
