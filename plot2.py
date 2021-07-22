with open("clean_data.csv", encoding="utf8", mode = "r") as fileClean:
    datas = fileClean.read().split("\n")

    #get header of csv file
    header = datas[0].split(",")
    #get subjects:
    subjects = header[5:] # number of subject = 16

    #get number of student:
    students = datas[1:]
    numberStudent = len(students)



# split each student in list:
for i in range(len(students)):
    students[i] = students[i].split(",")
#contain number of  students skip exam per subject
not_take_exam = [0]*16 # fl order subjects 

students.pop()

take_exam = [0]*12

for s in students:
    count = 0
    for i in range(5,16):
        if(s[i] != "-1"):
            count += 1
    take_exam[count] += 1
       

import matplotlib.pyplot as plt
import numpy as np
from numpy.core.fromnumeric import take

# -------------- piechart ----------------------
y = np.array(take_exam)
mylabels = [ "0 thi Môn nào","1 Môn", "2 Môn", "3 Môn", "4 Môn", "5 Môn", "6 Môn", "7 Môn", "8 Môn","9", "10", "11"]

fig1, axis = plt.subplots()
axis.pie(y, labels = mylabels, autopct='%1.1f%%',startangle=90)
axis.legend(title = "số môn mà học sinh thi")
axis.axis('equal')
plt.show() 

