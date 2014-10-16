f = open("new_scores.txt", "w")

'''
FINISH THIS;
    While loop to read in student names and grades; 'quit' to break
    write results to file
    close file
'''

while True:
    student = input("Enter Student's name: ")
    grade = input("Enter the student's grade: ")
    if student or grade == 'quit':
        break
    f.write(student + "," + grade)
    
f.close()
print("Thanks! We're done")