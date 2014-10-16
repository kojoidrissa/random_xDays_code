f = open("scores.txt", "r")
#I should change this to 'new_scores.txt', the file I'm creating
#with writing.py

students ={}

for line in f:
    entry = line.strip().split(",")
    student = entry[0]
    grade = entry[1]
    students[student] = grade
    print (student + ":" + grade)

f.close()

print()
print (students)
