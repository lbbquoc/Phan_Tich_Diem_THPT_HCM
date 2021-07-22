
#load unicode table
f =open('decode.txt', encoding= "utf8") 
unicode_table = f.read().split("\n")

for i in range(len(unicode_table)):
    unicode_table[i] = unicode_table[i].split("\t")
f.close()
# print(unicode_table[0].encode('utf-8'))
print(len(unicode_table[0]))


fWrite = open('unicode.txt', 'wb+')


for code in unicode_table:
    fWrite.write((code[1] + " " + code[2] + "\n").encode("utf-8"))

fWrite.close()

# chars = []
# codes = []
# dic_codes = dict()
# file = open("unicode.txt", encoding="utf8")
# unicode_table = file.read().split("\n")

# unicode_table.pop() # it have empty line at last element of list => error out of
#                     # range when split string

