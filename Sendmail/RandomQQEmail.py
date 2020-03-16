# 目标邮箱是随机生成一个9位数QQ号邮箱

import string
import random

def qq_email():
    digits = string.digits
    num = ""
    for i in range(1, 9):
        i += 1
        num += random.choice(digits)
        # print(num)
    qqEmail = num + "@qq.com"
    return qqEmail

    # qqlist = [qqEmail, '527539087@qq.com', '406556942@qq.com']
    # return qqlist

def random_char():
    letters = string.ascii_letters
    randsub = ''
    for i in range(1, 16):
        randsub += random.choice(letters)
    return randsub
