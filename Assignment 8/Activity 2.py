# This program takes input for grade and score from user
# and depend on that input it will calculate Average of those grades


def get_grade():
    print("Enter your grade :")
    grade = float(input())
    return grade


def get_score():
    print("Please Enter how many grades you want to enter:")
    score = float(input())
    return score


def display_score(total_grades, average):
    print("Sum of all grades enter by you :" + str(total_grades))
    print(f"Average of all your grades :{average:.2f}")


def get_average(total_grades, score):
    average = total_grades / score
    return average


def get_total_grades(total_grades, grade):
    sum_grade = total_grades + grade
    return sum_grade


def main():
    score = get_score()
    total_grades = 0
    flag = 1
    while(flag <= score):
        grade = get_grade()
        total_grades = get_total_grades(total_grades, grade)
        flag = flag + 1

    average = get_average(total_grades, score)
    display_score(total_grades, average)


main()
