#Le Ba Quoc - 18126008
#email : lbquoc.hue@gmail.com
# phone : 0398661333
import csv

# import subprocess
# start = 2000001
# end = 2074719

# res_minging_data = []
# for sbd in range(start,end):
#     command ='curl -F ' + '\"SoBaoDanh=0' + str(sbd) + '\"' + ' diemthi.hcm.edu.vn/Home/Show'
#     data = subprocess.check_output(command)
#     res_minging_data.append(data)

# with open("raw_data.txt", "a", newline="") as file_rawData:
#     writer = csv.writer(file_rawData)
#     writer.writerow(res_minging_data)

res_minging_data = []

def pre_clean_data(rawData):
    rawData = rawData.split("\\n")

    for i in range(len(rawData)): #remove redundant characters
        rawData[i] = rawData[i].replace("\\r","")
        rawData[i] = rawData[i].replace("\\t","")
        rawData[i] = rawData[i].strip() # remove space char first and last
    for i in range(len(rawData)): #remove tags html 
        tags =[]
        for j in range(len(rawData[i])):
            if rawData[i][j] == '<':
                begin = j
            if rawData[i][j] == '>':
                end = j
                tags.append(rawData[i][begin:end+1])
        for tag in tags:
            rawData[i] = rawData[i].replace(tag,"");
    
    unEmpty_line = [] # contain un empty line for clean
    for i in range(len(rawData)): 
        if rawData[i] != "":
            unEmpty_line.append(rawData[i])

    rawData = unEmpty_line # set rawData to un empty line 

    return rawData
    
def unicode_clean_data(rawData,sbd):
    #choose relevant infomation :
    name = rawData[7]
    dob = rawData[8]
    score = rawData[9]
    
    #load unicode table :
    chars = []
    codes = []

    file = open("unicode.txt", encoding= "utf8") #load unicode for encode
    unicode_table = file.read().split("\n")

    for code in unicode_table:
        x = code.split(" ") # it have format : char - code
        chars.append(x[0])
        codes.append(x[1])
    for i in range(len(chars)): # check and replace code to char ( name - score)
        name = name.replace(codes[i],chars[i])
        score = score.replace(codes[i],chars[i])
    for i in range(len(name)): # encode HTML code for NAME, format : &#...
        if name[i:i+2] == "&#":
            name = name[ : i] + chr(int(name[i+2 : i+5])) + name[i+6 : ]

    for i in range(len(score)): # encode HTML code for SCORE, format : &#...
        if score[i:i+2] == "&#":
            score = score[ : i] + chr(int(score[i+2 : i+5])) + score[i+6 : ]
    
    # convert string to lower
    name = name.lower()
    score = score.lower()
    list_dob = dob.split("/")

    #split date of birh
    dd = list_dob[0]
    mm = list_dob[1]
    yy = list_dob[2]

    #split score:
    score = score.replace(":","")
    score = score.replace("khxh ","khxh   ") #because of format of HTML
    score = score.replace("khtn ","khtn   ") #because of format of HTML

    list_score = score.split("   ") # split score after handling string score

    #create dictionary or persional socre -- for add to file 
    dict_score = dict()
    for i in range(0,len(list_score) - 1,2):
        dict_score[list_score[i]] = list_score[i+1]
    
    data = [sbd,name.title(),dd,mm,yy] # prepare format to write data to file 
    
    #add subjects to data for write on file
    list_subjects = ["toán","ngữ văn","khxh","khtn","lịch sử","địa lí", "gdcd", "sinh học","vật lí","hóa học","tiếng anh","tiếng nhật", "tiếng pháp", "tiếng trung","tiếng đức","tiếng nga"]
    
    for subject in list_subjects:
        if subject in dict_score:
            data.append(dict_score[subject])
        else:
            data.append("-1")
    
    return data
        
def get_clean_data(data):
    with open("clean_data.csv","a",encoding="utf8", newline="") as file_csv:
        writer = csv.writer(file_csv)
        writer.writerow(data)


# read ignore sbd because of not valid
file = open("ignore_sbd.txt", "r")
ignoreList = file.read().split("\n")
for i in range(len(ignoreList)):
    ignoreList[i] = int(ignoreList[i])

#read all data in a raw_data file
file = open("raw_data.txt", "r" )
rawDatas = file.read().split("\n")
sbd = 2000000

with open("clean_data.csv", encoding="utf8", mode= "w", newline="") as file_csv:
    header = ["sbd","name","dd","mm","yy","toán","ngữ văn","khxh","khtn","lịch sử","địa lí", "gdcd", "sinh học","vật lí","hóa học", "tiếng anh", "tiếng nhật", "tiếng pháp", "tiếng trung","tiếng đức","tiếng nga"]
    writer = csv.writer(file_csv)
    writer.writerow(header) 

for rawData in rawDatas:
    sbd += 1
    if sbd in ignoreList:
        continue
    sbd_str = "0" + str(sbd)
    rawData = pre_clean_data(rawData)
    data = unicode_clean_data(rawData,sbd_str)
    # print(data)
    get_clean_data(data)


            

