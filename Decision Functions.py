def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 75:
        return "C"
    else:
        return "Failed"

grade = float(input("Enter your grade: "))
print("Grade: ", get_grade(grade))
