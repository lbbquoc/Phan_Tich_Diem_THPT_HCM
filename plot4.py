from os import symlink
from numpy.core.numeric import count_nonzero
from numpy.lib.function_base import average


with open("clean_data.csv", encoding="utf8", mode="r") as fileClean:
    datas = fileClean.read().split("\n")

    # get header of csv file
    header = datas[0].split(",")
    # get subjects:
    subjects = header[5:]  # number of subject = 16

    # get number of student:
    students = datas[1:]
    numberStudent = len(students)


# split each student in list:
for i in range(len(students)):
    students[i] = students[i].split(",")

#remove last student (empty student)    
students.pop()

#get number of student per age group
# 17 18 19 ... 27 , quy dinh nhu vay 
number_of_student_per_age_group = [0]*11
average_of_student_per_age_group = [0]*11

for s in students:
    age = 2020 - int(s[4])
    if age >= 27:
        age = 27
    number_of_student_per_age_group[age - 17] += 1

    sum_score = 0
    count_score = 0
    for i in range(11):
        if s[i + 5] != "-1":
            sum_score += float(s[i+5])
            count_score += 1
    if count_score == 0:
        continue
    average = sum_score/count_score
    average_of_student_per_age_group[age - 17] += average

# cal average score per age group
for i in range(len(average_of_student_per_age_group)):
    if number_of_student_per_age_group[i] != 0:
        average = average_of_student_per_age_group[i]
        num = number_of_student_per_age_group[i]
        average_of_student_per_age_group[i] = average/num
# make number for average list to draw line chart
for i in range(len(average_of_student_per_age_group)):
    average_of_student_per_age_group[i] = average_of_student_per_age_group[i] * 7000

print(number_of_student_per_age_group)
print(average_of_student_per_age_group)
# # -------------- draw chart -----------------
import matplotlib.pyplot as plt
import numpy as np

New_Colors = ["green", "blue", "purple", "brown", "teal"]


figure, axis = plt.subplots()

# list subjects from 0-15
y_pos = np.arange(11)
x_pos = np.arange(11)

age = [17,18,19,20,21,22,23,24,25,26," >26 Tuổi"]


# plot the barchart using 2 list
plt.bar(y_pos, number_of_student_per_age_group, align="center", alpha=0.5, color=New_Colors)
plt.plot(x_pos, average_of_student_per_age_group, color ="red", marker="o")

# change horizontal category name
plt.xticks(x_pos, age)

# set limit to vertical axis
axis.set_ylim(0, 70000)

# label and title
axis.set_ylabel("Số học sinh  ")
axis.set_xlabel("Tuổi ")

#right side ticks

ax2 = axis.twinx()
ax2.tick_params('y',color = 'red')
ax2.set_ylabel("Điểm trung bình")
ax2.set_ylim(0,10)

plt.title("Điểm trung bình theo độ tuổi ")


# draw numbers of student on top of the each bar
rects = axis.patches
for rect, label in zip(rects, number_of_student_per_age_group):
    height = rect.get_height()
    axis.text(
        rect.get_x() + rect.get_width() / 2, height + 0.5 , label, ha="center", va="bottom"
    )
# show plot
plt.show()
