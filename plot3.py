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

num_of_exam_taken = [0] * 12

average = [0] * 12

students.pop()

for s in students:
    count = 0
    total = 0
    for i in range(12):
        if s[i + 5] != "-1":
            total += float(s[i + 5])
            count += 1
    if count == 0:
        continue
    num_of_exam_taken[count] += 1
    average[count] += total / count


for i in range(len(average)):
    if num_of_exam_taken[i] != 0:
        average[i] = round(average[i] / num_of_exam_taken[i], 2)

print(average)
print(num_of_exam_taken)


import matplotlib.pyplot as plt
import numpy as np

New_Colors = ["green", "blue", "purple", "brown", "teal"]


figure, axis = plt.subplots()

# list subjects from 0-15
y_pos = np.arange(12)
x_pos = np.arange(12)

# plot the barchart using 2 list
plt.bar(x_pos, average, align="center", alpha=0.5, color=New_Colors)

# change horizontal category name
plt.xticks(x_pos, y_pos)

# set limit to vertical axis
axis.set_ylim(0, 10)

# label and title
plt.ylabel("Điểm Trung Bình   ")
plt.title("Số học sinh bỏ thi hoặc không đăng ký ")


# draw numbers of student on top of the each bar
rects = axis.patches
for rect, label in zip(rects, average):
    height = rect.get_height()
    axis.text(
        rect.get_x() + rect.get_width() / 2,
        height + 0.5,
        label,
        ha="center",
        va="bottom",
    )
# show plot
plt.show()
