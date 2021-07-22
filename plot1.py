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
# contain number of  students skip exam per subject
not_take_exam = [0] * 16  # fl order subjects

students.pop()
for s in students:
    for i in range(5, 21):
        if s[i] == "-1":
            not_take_exam[i - 5] += 1  # minus 5 elements not exam

not_take_exam_percentage = [0] * 16
for i in range(16):
    not_take_exam_percentage[i] = round(not_take_exam[i] / numberStudent * 100, 2)
print(not_take_exam_percentage)


# take not_take_exam_percentage and subjects


import matplotlib.pyplot as plt
import numpy as np

New_Colors = ["green", "blue", "purple", "brown", "teal"]


figure, axis = plt.subplots()

# list subjects from 0-15
y_pos = subjects

# plot the barchart using 2 list
plt.bar(y_pos, not_take_exam_percentage, align="center", alpha=0.5, color=New_Colors)

# change horizontal category name
plt.xticks(y_pos, subjects)

# set limit to vertical axis
axis.set_ylim(0, 100)

# label and title
plt.ylabel("Tỉ lệ")
plt.title("Số học sinh bỏ thi hoặc không đăng ký ")


# draw numbers of student on top of the each bar
rects = axis.patches
for rect, label in zip(rects, not_take_exam):
    height = rect.get_height()
    axis.text(
        rect.get_x() + rect.get_width() / 2, height + 3, label, ha="center", va="bottom"
    )
# show plot
plt.show()
