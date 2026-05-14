row_count = int(input())

for i in range(row_count):
    student_count, *grade_list = input().split()

    student_count = int(student_count)
    grade_list = [int(x) for x in grade_list]

    average = sum(grade_list) / student_count

    total_passing_students = 0

    for grade in grade_list:
        if grade > average:
            total_passing_students += 1

    percentage = total_passing_students / student_count * 100

    print(f"{(percentage):.3f}%")
