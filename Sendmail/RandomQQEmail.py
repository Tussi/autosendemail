import string
import random

# 随机生成一个9位数QQ号邮箱
def qq_email():
    digits = string.digits
    num = ""
    for i in range(1, 9):
        i += 1
        num += random.choice(digits)
        # print(num)
    qqEmail = num + "@qq.com"
    qqlist = [qqEmail, '527539087@qq.com', '406556942@qq.com']
    # print(qqEmail)
    # return qqlist
    return qqEmail

def random_char():
    letters = string.ascii_letters
    randsub = ''
    for i in range(1, 16):
        randsub += random.choice(letters)
    return randsub
