def gradeCalc(hws, quizlets, midterm_1, midterm_2, final):

    hw_sum = 0
    for hw in hws:
        hw_sum += hw
    hw_avg = hw_sum/(len(hws) * 50)

    quizlet_sum = 0
    for quiz in quizlets:
        quizlet_sum += quiz
    quizlet_avg = quizlet_sum/(len(quizlets) * 5)

    grade = (0.3 * hw_avg) + (0.1 * quizlet_avg) + (0.2 * (midterm_1/100)) + (0.2 * (midterm_2/100)) + (0.2 * (final/100)) + 0.01

    letter = ""

    if grade >= 0.93:
        letter = "A"
    elif grade >= 0.90 and grade < 0.93:
        letter = "A-"
    elif grade >= 0.87 and grade < 0.90:
        letter = "B+"
    elif grade >= 0.83 and grade < 0.87:
        letter = "B"
    elif grade >= 0.80 and grade < 0.83:
        letter = "B-"
    elif grade >= 0.77 and grade < 0.80:
        letter = "C+"
    elif grade >= 0.73 and grade < 0.77:
        letter = "C"
    elif grade >= 0.70 and grade < 0.73:
        letter = "C-"
    elif grade >= 0.67 and grade < 0.70:
        letter = "D+"
    elif grade >= 0.63 and grade <= 0.66:
        letter = "D"
    elif grade >= 0.60 and grade <= 0.62:
        letter = "D-"
    else:
        letter = "F"

    return "Your Grade is: " + letter + " (" + str((float(grade)) * 100) + " %" + ")"


print(gradeCalc([30.00, 33.00, 45.00, 44.00, 36.00, 44.00, 44.33, 38.00, 41.00, 38.00, 41.83], [2.50, 3.00, 5.00, 5.00, 5.00, 5.00, 5.00, 3.33, 5.00, 5.00, 5.00, 5.00], 62, 51, 65))
