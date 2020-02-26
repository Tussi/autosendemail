import csv
import random

def get_mail_qq():
    csv_file = csv.reader(open('D:/Downloads/Scripts/AutoSendEmail_script/Resource/USender.csv', encoding='utf-8'))
    qqmlist = []
    for row in csv_file:
        qqmlist.append(row)
    # return qqmlist

    #随机获取一个邮箱
    qqm = random.choice(qqmlist)
    print(qqm)
    return qqm[0], qqm[1]
