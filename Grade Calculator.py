# Input
code = int(input("Enter the Code Grade:"))
test = int(input("Enter the Test Grade:"))
late = int(input("Enter the Days Late up to 2:"))

# Process
if late == 0:
    raw_grade = code + test
    final_grade = raw_grade
elif late == 1 or late == 2:
    raw_grade = code + test
    final_grade = raw_grade - (late * 5)
else:
    print(f"Not more than 2 days late!")

# Output

print(f"Code:{code}, Test:{test}, Raw Grade:{raw_grade}, Late:{late}, Final:{final_grade}")
