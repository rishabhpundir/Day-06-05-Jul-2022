# 01. Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up. 

# from array import array


# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())

#     score_list = list(arr)
#     score_list.sort()
#     runner_up = 0
#     winner = score_list[len(score_list)-1]

#     for i in range(0, len(score_list)):
#         for j in range(i+1, len(score_list)):
#             if score_list[i] < score_list[j] and score_list[i] < winner:
#                 runner_up = score_list[i]

#     print(runner_up)


# ---------------------------------------------------------------------------------------------------------------------------------------


# 02. Given the names and grades for each student in a class of n students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]] 
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# student = []
# student_list = [] 
# grades_list = []
# students = []

# total_students = int(input('Enter the total number of students in your class : '))

# for i in range(0, total_students):
#     name = str(input(f'Enter student name {i+1} : '))
#     grades = float(input(f'Enter student grade (out of 50.00) : '))
#     student = [name, grades]
#     grades_list.append(grades)
#     student_list.append(student)

# grades_list.sort()
# second_lowest = grades_list[1]

# for j in range(0, total_students):
#         for k in range(j, total_students):
#             if grades_list[k] >= grades_list[j]:
#                 if grades_list[k] > grades_list[j]:
#                     second_lowest = grades_list[k]
#                     break
#                 elif grades_list[k] == grades_list[-1]:
#                     second_lowest = grades_list[k] 
#                     break
#         break
                    
# for student in student_list:
#     if student[1] == second_lowest:
#         students.append(student[0])

# students.sort()
# print('The student(s) with the second lowest grades : ')
# for i in students:
#     print(i)


# ---------------------------------------------------------------------------------------------------------------------------------------




