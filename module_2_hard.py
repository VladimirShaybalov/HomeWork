import random

colum = random.randint(3,20)
string = ''


for k in range(2, 21):
    string = ''
    for i in range(1, colum):
        for j in range(i +1,colum):
            if colum % (i + j) == 0:
                string += str(i) + str(j)
print(colum, '-',string)


