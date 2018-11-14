def gradeCalc(hws, quizlets, midterm_1, midterm_2, final):

    hw_sum = 0
    for hw in hws:
        hw_sum += hw
    hw_avg = hw_sum/(len(hws) * 50)

    quizlet_sum = 0
    for quiz in quizlets:
        quizlet_sum += quiz
    quizlet_avg = quizlet_sum/(len(quizlets) * 5)

    grade = (0.3 * hw_avg) + (0.1 * quizlet_avg) + (0.2 * (midterm_1/100)) + (0.2 * (midterm_2/100)) + (0.2 * (final/100))

    return "Your Grade is: " + str(float(grade) + 0.01)


print(gradeCalc([45.00, 30.00, 44.00, 36.00, 44.00, 33.00, 44.33, 38.00, 41.00], [5.00, 2.50, 3.00, 5.00, 5.00, 5.00, 5.00, 3.33, 5.00, 5.00], 62, 51, 65))
