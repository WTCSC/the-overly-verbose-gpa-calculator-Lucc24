while True:
    firstsemask = input(str("\nGreetings, ambitious scholar! Please bestow upon this humble calculator the magnificent numerical representations of your first semester's academic achievements. \n Please ensure a minimum of 5 glorious grades separated by spaces on the sacred 4.0 scale (such as 4.0 3.0 2.0, etc): "))
    secondsemask = input(str("\nNow, esteemed pupil, kindly illuminate this program with the spectacular grades from your second semester of intellectual conquest.\n Once again i am requiring no fewer than 5 numerical inputs separated by spaces on the 4.0 scale (such as 4.0 3.0 2.0, etc): "))
    gradesask = firstsemask + secondsemask
    try:
        firstgrades = [float(grade) for grade in firstsemask.split()]
        secondgrades = [float(grade) for grade in secondsemask.split()]
    except ValueError:
        print("\nAlas! The mystical computational spirits have detected non-numerical entities in your input! \nThis extraordinary calculator requires only the purest of numeric values to perform its mathematical wizardry. Please rectify this situation post-haste!")
        continue

    if any(grade < 0.00 or grade > 4.00 for grade in firstgrades + secondgrades):
        print("\nOh dear! It appears that some of your academic measurements have ventured beyond the sacred boundaries of the 4.0 scale! \nThis magnificent calculator can only process grades dwelling within the range of 0.00 to 4.00. Please recalibrate your inputs!")
        continue

    if len(firstgrades) < 5 or len(secondgrades) < 5:
        print("\nMagnificent student! Your academic journey requires a minimum of 5 spectacular grades per semester for this calculator to perform its so very accurate computational sorcery. \nPlease provide the full amount of grades!")
        continue

    gpa_first_half = sum(firstgrades) / len(firstgrades)
    gpa_second_half = sum(secondgrades) / len(secondgrades)
    gpa = sum(firstgrades + secondgrades) / len(firstgrades + secondgrades)
    
    print(f"\nBEHOLD! After performing extraordinarily complex mathematical computations that would make ancient scholars cry to their mamas, your magnificent overall Grade Point Average stands triumphantly at: {gpa:.3f}!")
    semesterask= input(str("\nNow, distinguished learner, upon which semester of your academic journey would you prefer this calculator to focus its infinite wisdom? ")).strip().lower()
    if "first" in semesterask or "1" in semesterask:
        print(f"\nAh, the first semester! That initial chapter of your educational journey yielded a spectacular GPA of: {gpa_first_half:.3f}!")
    elif "second" in semesterask or "2" in semesterask:
        print(f"\nThe second semester! That magnificent continuation of your scholarly quest produced a remarkable GPA of: {gpa_second_half:.3f}!")
    if gpa_first_half > gpa_second_half:
        print("\nAlas! The winds of academic fortune have shifted, and your GPA experienced a slight decline during the second semester of your educational journey. Fear not, noble scholar, for every great mind faces such challenges!")
    elif gpa_first_half < gpa_second_half:
        print(f"\nMAGNIFICENT! Your academic prowess has soared to new heights! Your GPA experienced a truly spectacular improvement in the second half of the semester from {gpa_first_half:.3f} to {gpa_second_half:.3f}!")
    elif gpa_first_half == gpa_second_half:
        print("\nRemarkable consistency, dear student! Your GPA has maintained its steady course throughout both semesters, showing the admirable stability of a true academic warrior!")
    while True:
        goalask = input(str("\nNow, impeccable student, please reveal unto this calculator the summit you aspire to reach - what magnificent target GPA do you seek to achieve? ")).strip()
        try:
            target_gpa = float(goalask)
        except ValueError:
            print("\nOh my! The computational spirits are perplexed by your input! This calculator requires a pure numerical value to represent your target GPA. Please enlighten us with digits!")
            continue
        if target_gpa < 0.00 or target_gpa > 4.00:
            print("\nNoble person! Your target must reside within the sacred realm of 0.00 to 4.00 for this calculator to perform its mystical analysis!")
            continue
        if gpa >= target_gpa:
            print("GLORIOUS ACHIEVEMENT! You have not merely met but have triumphantly surpassed your target GPA! Your academic excellence knows no bounds, magnificent scholar!")
    
    

        all_grades = firstgrades + secondgrades
        possible_improvements = []
        print("\nThis magnificent calculator shall now embark upon a thrilling analytical expedition to determine whether your terrible GPA aspirations can be achieved by elevating individual academic achievements to a 4.0!")
        for i in range(len(all_grades)):
            original_grade = all_grades[i]
            if original_grade < 4.0:
                temp_grades = all_grades.copy()
                temp_grades[i] = 4.0
                new_gpa = sum(temp_grades) / len(temp_grades)
                improvement = new_gpa - gpa
                print(f"Class #{i+1}: Current grade = {original_grade} ---> 4.0 = GPA {new_gpa:.2f} ( +{improvement:.2f} points)!")
                if new_gpa >= target_gpa:
                    possible_improvements.append(i+1)
            else:
                print(f"Class #{i+1}: Your grade of {original_grade} already dwells at the summit of academic perfection!")

        if possible_improvements:
            print(f"\nEUREKA! The mathematical gods have spoken! You possess multiple pathways to academic glory! By elevating ANY of the following classes to the magnificent pinnacle of 4.0, you shall triumphantly reach your coveted target GPA of {target_gpa}:")
            for class_num in possible_improvements:
                print(f"Class #{class_num} -  get this to a 4.0!")
        else:
            print(f"\nThe computational analysis reveals that achieving your possibly overly ambitious target GPA of {target_gpa} through the improvement of merely one class to 4.0 lies beyond the realm of possibility.")
            againask = input(str("\nWould you like to attempt a different target GPA, noble scholar? (yes/no): ")).strip().lower()
            if againask == "yes" or againask == "y":
                continue
            elif againask == "no" or againask == "n":
                ask = input(str("\nWould you like to start a new GPA calculation? (yes/no): ")).strip().lower()
                if ask == "yes" or ask == "y":
                    break
                elif ask == "no" or ask == "n":
                    exit()
                    break
            
        break
    
    
    