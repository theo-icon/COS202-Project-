# PERSONAL POCKET CGPA CALCULATOR (PPC)

def get_grade_point(grade):
    grade = grade.upper()
    if grade == "A":
        return 5
    elif grade == "B":
        return 4
    elif grade == "C":
        return 3
    elif grade == "D":
        return 2
    elif grade == "E":
        return 1
    elif grade == "F":
        return 0
    else:
        return None


def cgpa_calculator():
    print("==== PERSONAL POCKET CGPA CALCULATOR ====")

    total_units = 0
    total_points = 0

    while True:
        course = input("\nEnter course name (or type 'done' to finish): ")

        if course.lower() == "done":
            break

        try:
            unit = int(input("Enter course unit: "))
        except ValueError:
            print("Invalid unit!")
            continue

        grade = input("Enter grade (A-F): ")
        point = get_grade_point(grade)

        if point is None:
            print("Invalid grade!")
            continue

        total_units += unit
        total_points += unit * point

    if total_units == 0:
        print("No courses entered.")
    else:
        cgpa = total_points / total_units
        print("\n==== RESULT ====")
        print("Total Units:", total_units)
        print("Total Points:", total_points)
        print("CGPA:", round(cgpa, 2))


# Run program
cgpa_calculator()