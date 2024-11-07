print("Welcome to the Student Grading Service")
print()  # Added blank lines to make the program look better

# Get student ID
student_id = input("What is the student ID number? ")
while not student_id.isdigit():
    print("Invalid input. Please enter an integer.")
    student_id = input("What is the student ID number? ")
student_id = int(student_id)
print()

# Get valid code grade between 0 and 100
code = -1
while code < 0 or code > 100:
    grade_input = input("Enter the Code Grade (0-100): ")
    while not grade_input.isdigit():
        print("Invalid input. Please enter an integer.")
        grade_input = input("Enter the Code Grade (0-100): ")
    code = int(grade_input)
    if code < 0 or code > 100:
        print("Invalid input. Please enter a grade between 0 and 100.")

# Get valid test grade between 0 and 100
test = -1
while test < 0 or test > 100:
    grade_input = input("Enter the Test Grade (0-100): ")
    while not grade_input.isdigit():
        print("Invalid input. Please enter an integer.")
        grade_input = input("Enter the Test Grade (0-100): ")
    test = int(grade_input)
    if test < 0 or test > 100:
        print("Invalid input. Please enter a grade between 0 and 100.")

# Get the number of days late (0 to 2)
late = -1
while late < 0 or late > 2:
    late_input = input("Enter the Days Late (0-2): ")
    while not late_input.isdigit():
        print("Invalid input. Please enter an integer.")
        late_input = input("Enter the Days Late (0-2): ")
    late = int(late_input)
    if late < 0 or late > 2:
        print("Invalid input. Please enter a number between 0 and 2.")

# Process the grading
raw_grade = code + test

# Apply late penalty
if late == 0:
    final_grade = raw_grade
else:
    final_grade = raw_grade - (late * 5)

print()

# Output
print(f"Student Number: {student_id}, Code: {code}, Test: {test}, Raw Grade: {raw_grade}, Days Late: {late}, Final Grade: {final_grade}")
print()
print("Grading completed, thank you for using SGS.")
