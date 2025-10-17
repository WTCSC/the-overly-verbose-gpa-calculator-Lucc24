while True:
    gradesask = input(str("Enter a minimum of 5 grades separated by spaces in a 4.0 scale (4.0,3.0,2.0, etc): "))

    try:
        grades = [float(grade) for grade in gradesask.split()]
    except ValueError:
        print("Invalid input. Please enter numeric grades only.")
        continue

    if any(grade < 0.00 or grade > 4.00 for grade in grades):
        print("Please enter valid grades between 0.00 and 4.00.")
        continue

    if len(grades) < 5:
        print("Please enter at least 5 grades.")
        continue
    first_half = grades[:len(grades)//2]
    second_half = grades[len(grades)//2:]
    gpa_first_half = sum(first_half) / len(first_half)
    gpa_second_half = sum(second_half) / len(second_half)
    gpa = sum(grades) / len(grades)
    
    print(f"based on your {len(grades)} grades, your GPA is: {gpa}")
    semesterask= input(str("Which semester would you like to focus on? (first half or second half of grades) ")).strip().lower()
    if semesterask == "first":
        print(f"Your GPA for the first half of the semester is: {gpa_first_half}")
    elif semesterask == "second":
        print(f"Your GPA for the second half of the semester is: {gpa_second_half}")
    if gpa_first_half > gpa_second_half:
        print("Your GPA improved in the second half of the semester!")
    elif gpa_first_half < gpa_second_half:
        print("Your GPA declined in the second half of the semester.")
    break
