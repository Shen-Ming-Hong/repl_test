students = {'tom': 85, 'mary': 76, 'joe': 58}
print('學生數 = {}'.format(len(students)))
print('{} 總分 = {}'.format(
    str(list(students.values())).replace(',', ' ')[1:-1],
    sum(students.values())))
print('平均 = {}'.format(sum(students.values()) / len(students)))
