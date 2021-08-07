students = tuple(['tom', 'mary', 'joe'])
students_grades = tuple([85, 76, 58])
print('學生數 = {}'.format(len(students)))
print('{} 總分 = {}'.format(
    str(students_grades).replace(',', ' ')[1:-1], sum(students_grades)))
print('平均 = {}'.format(sum(students_grades) / len(students)))
student_index = int(input('請入整數學號 => '))
print("姓名 = {}".format(students[student_index]))
print("成績 = {}".format(students_grades[student_index]))