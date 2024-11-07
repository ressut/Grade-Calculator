print("Student Grading Service")
print()

# Get student ID
student_id = int(input("What is your student ID number? "))
print()
print(f"Welcome student number {student_id}")
print()

# Get valid code grade between 0 and 100
code = -1  # Start with an invalid value to enter the loop
while code < 0 or code > 100:
    code = int(input("Enter the Code Grade (0-100): "))
    if code < 0 or code > 100:
        print("Invalid input. Please enter a grade between 0 and 100.")

# Get valid test grade between 0 and 100
test = -1  # Start with an invalid value to enter the loop
while test < 0 or test > 100:
    test = int(input("Enter the Test Grade (0-100): "))
    if test < 0 or test > 100:
        print("Invalid input. Please enter a grade between 0 and 100.")

# Get the number of days late (0 to 2)
late = -1 # Start with an invalid value to enter the loop
while late < 0 or late > 2:
    late = int(input("Enter the Days Late (0-2): "))
    if late < 0 or late > 2:
        print("Invalid input. Please enter a number between 0 and 2.")

# Process the grading
raw_grade = code + test
        
# Apply late penalty
if late == 0:
    final_grade = raw_grade
elif 1 <= late <= 2:
    final_grade = raw_grade - (late * 5)
else:
    print("Days late penalty only applies up to 2 days.")
    final_grade = raw_grade

# Output
print(f"Code: {code}, Test: {test}, Raw Grade: {raw_grade}, Late: {late}, Final Grade: {final_grade}")
print()
print("Grading completed and thank you for using SGS.")
exit()
