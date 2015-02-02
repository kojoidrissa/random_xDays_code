f = open("new_scores.txt", "w")

'''
FINISHED THIS;
    While loop to read in student names and grades; 'quit' to break
    write results to file
    close file
'''

while True:
    student = input("Enter Student's name: ")
    if student == 'quit':
        print("Thanks! We're done")
        break
    grade = input("Enter the student's grade: ")
    f.write(student + "," + grade + "\n")

f.close()
