grades = [[5, 3, 3, 5, 4],
          [2, 2, 2, 3],
          [4, 5, 5, 2],
          [4, 4, 3],
          [5, 5, 5, 4, 5]]
students = {'Johnny',
            'Bilbo',
            'Steve',
            'Khendrik',
            'Aaron'}
students = (list(students))
students.sort()
students_dict = {}
scores = []

count = 0
while count < len(grades):
    march_list = grades[count]
    average_score = sum(march_list)/len(march_list)
    student = students[count]
    students_dict[student] = average_score
    count = count + 1
print(students_dict)