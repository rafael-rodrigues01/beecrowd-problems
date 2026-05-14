row_count = int(input())

for _ in range(row_count):
    student_count, *grade_list = input().split()

    student_count = int(student_count)
    grade_list = [int(x) for x in grade_list]

    average = sum(grade_list) / student_count

    students_above_average = 0

    for grade in grade_list:
        if grade > average:
            students_above_average += 1

    percentage = students_above_average / student_count * 100

    print(f"{percentage:.3f}%")
