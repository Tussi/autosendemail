# coding=utf-8
import smtplib
import mimetypes
import time
import datetime
import random

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.header import Header
from email.utils import formataddr

# 引入外部文件
from Common.log import *
from Sendmail.getMailQQ import get_mail_qq
from Sendmail.RandomQQEmail import qq_email, random_char
from Sendmail.randCont import randCont
from Sendmail.CheckEmail import checkInbox


#目录主位置
_root_dir = 'D:/Downloads/Scripts/AutoSendEmail_script'
_title_common = 'happy new year'

#发收邮箱smtp地址
_smtp_address = ['smtp.163.com', 'smtp.126.com', 'smtp.qq.cn', 'smtp.sina.com', 'smtp.gmail.com']
_pop_address = ['pop.163.com', 'pop.126.com', 'pop.qq.cn', 'pop.sina.com', 'pop.gmail.com']



def sendMail(sender, recivers, subject, content, passwd, smtp_srv):
    username = sender
    password = passwd
    reciver = recivers
    print(reciver)
    msg = MIMEMultipart('related')
    msg['Subject'] = subject
    # html格式
    html = content
    htm = MIMEText(html, 'html', 'utf-8')
    msg.attach(htm)
    # # 构造图片
    # fp = open(_root_dir + 'Image/logo_small.png', 'rb')
    # msgImage = MIMEImage(fp.read())
    # fp.close()
    # msgImage.add_header("Content-ID", "<image1>")
    # msg.attach(msgImage)
    # fp2 = open(_root_dir + 'Image/yurenjie.png', 'rb')
    # msgImage2 = MIMEImage(fp2.read())
    # fp2.close()
    # msgImage2.add_header('Content-Disposition', 'attachment',
    #                      filename="愚人节活动海报.jpg")
    # msg.attach(msgImage2)
    # header_from = Header("moumou的小号", 'utf-8')
    header_from = formataddr([NameS, username], "utf-8")
    msg['From'] = header_from

    # header_to = Header("皮皮的小号", 'utf-8')
    header_to = formataddr([NameR, reciver], "utf-8")
    msg['To'] = header_to

    # 发送邮件
    if "@qq.com" in username:
        print(smtp_srv)
        smtp = smtplib.SMTP_SSL(smtp_srv.encode(), 465)
        print(smtp)
        print("qq")
        smtp.login(username, password)
        smtp.sendmail(username, reciver, msg.as_string())
        smtp.quit()

    else:
        smtp = smtplib.SMTP()
        smtp.connect(smtp_srv)
        # smtp.ehlo()
        # smtp.starttls()
        smtp.login(username, password)
        smtp.sendmail(username, reciver, msg.as_string())
        smtp.quit()

    # 读取文件中的数据，并将使用,分割的数据变为数组
    def readFileToSplit(filepath):
        file_stream = open(filepath)
        try:
            data = file_stream.read()
        finally:
            file_stream.close()
        data_split = data.split(',')
        return data_split

if __name__ == "__main__":
    j = 0
    while j < 2:
        # content = _content
        # 接收人的邮箱按照每天2000封来，每天的邮箱都需要更换，文件名最后以日期为准，邮件发送量以日志为准
        # recivers = qq_email()
        # 把4个邮箱的账号都获取到，方便下面for循环中使用

        # log_file_stream = open(_root_dir+'log', 'w+')
        logger.info('')
        logger.info('脚本开始------------------------------------------------------------------')

        # 统计邮件发送量
        arr_num = 0
        send_num = 0
        send_numb = 0
        # 统计发送出错量
        error_num = 0
        # 统计发送成功的邮箱发送账号
        send_success_account = []
        # 统计发送失败的邮箱发送账号
        send_failure_account = []

        # 最后统计没有发出去的邮箱号，放到下日，继续发送
        for i in range(0, 448):  # 数字填写邮箱的个数，尽量每一个都邮箱使用到
            # 邮箱内容设置
            NameS, NameR, Subj, Cont = randCont()
            content = random_char() + Cont + random_char()
            recivers = qq_email()
            if i == 0:
                recivers = "527539087@qq.com"  # 指定接收邮箱
            elif i == 1:
                recivers = "hohoyo789@gmail.com"  # 指定接收邮箱2
            print(recivers)
            subject = Subj + "-----" + random_char()  # 获取随机主题+随机一串字母

            try:
                # sendindex = i - error_num
                # num = i % 30
                # allsender = get_mail_qq()[i]
                # mail_username, mail_pwd = allsender[0], allsender[1]
                mail_username, mail_pwd = get_mail_qq()
                # Debug发件箱
                # mail_username, mail_pwd = "ku8u89@gmail.com", "aa789123"
                if "@163.com" in mail_username:
                    account = mail_username
                    pwd = mail_pwd
                    smtpadd = _smtp_address[0]
                    popadd = _pop_address[0]
                    print(account, pwd, smtpadd, popadd)
                    send_num += 1
                    print(send_num)
                elif "@126.com" in mail_username:
                    account = mail_username
                    pwd = mail_pwd
                    smtpadd = _smtp_address[1]
                    popadd = _pop_address[1]
                    print(account, pwd, smtpadd,popadd)
                    send_num += 1
                    print(send_num)
                # if "@qq.com" in mail_username:
                #     account = '406556942@qq.com'   # mail_username
                #     pwd = 'yexurpjmpnrhbhfa'   # mail_pwd
                #     # pwd = 'binXI513021'
                #     smtpadd = _smtp_address[2]
                #     popadd = _pop_address[2]
                #     print(account, pwd, smtpadd,popadd)
                elif "@sina.com" in mail_username:
                    account = 'ss13126325@sina.com'  # mail_username
                    pwd = '7ac1593dac2d4493'  # mail_pwd
                    smtpadd = _smtp_address[3]
                    popadd = _pop_address[3]
                    print(account, pwd, smtpadd, popadd)
                    send_num += 1
                elif "@gmail.com" in mail_username:
                    account = mail_username
                    pwd = mail_pwd
                    smtpadd = _smtp_address[4]
                    popadd = _pop_address[4]
                    print(account, pwd, smtpadd,popadd)
                    send_num += 1
                    print(send_num)
                else:
                    continue
                print(send_num)
                sender = account
                passwd = pwd
                smtp_srv = smtpadd
                pop_srv = popadd
                # smtpstr=str('163')
                sendMail(sender, recivers, subject, content, passwd, smtp_srv)
                # print('发送账号', sender, '正在发送')
                str_success_1 = '发送账号【' + sender + '】正在发送'
                logger.info(str_success_1)
                # writeLog(log_file_stream,str_success_1)
                # print('接收序号', i, recivers[i],'发送成功')
                str_success_2 = '接受序号【' + str(send_num-error_num) + '】【' + recivers + '】发送成功'
                # writeLog(log_file_stream,str_success_2)
                logger.info(str_success_2)
                logger.info('')
                # print('')
                # send_num += 1

                # 提取可用邮箱
                # acc = sender + "," + passwd
                # print(acc)
                # with open(r"D:/Downloads/Scripts/AutoSendEmail_script/Sendmail/USender.txt", "a") as f:
                #     f.write(acc + '\n')
                # f.close()
                time.sleep(90)
                print("checkInbox..........")
                # 检查收件箱是否有退信，如果有退信，则表示发送不成功
                timediff = checkInbox(sender, passwd, pop_srv)
                # print(timediff)
                if timediff <= 150:
                    print("%s秒前收到最新邮件"% timediff)
                    arr_num += 1
                    print("%s封邮件没有到达！" % arr_num)
                else:
                    print("邮件已送达！")
                    send_success_account.append(sender)
                time.sleep(60)
            except Exception as e:
                # print('停止于：', i, recivers[i],',发送失败')
                str_failure_1 = '产生错误于：【' + sender + '】发送失败'
                # writeLog(log_file_stream,str_failure_1)
                logger.error(str_failure_1)
                # print(e)
                str_failure_2 = str(e)
                # writeLog(log_file_stream,str_failure_2)
                logger.error(str_failure_2)
                logger.info('')
                error_num += 1
                send_failure_account.append(sender)
                # print('')
                # break
        # print('安全抵达底部')
        # writeLog(log_file_stream,'脚本结束')
        set(send_success_account)
        set(send_failure_account)
        logger.info('邮件总数量【' + str(send_num) + '】')
        logger.info('总计发送邮件数量【' + str(send_num-error_num) + '】')
        logger.info('总计邮件送达数量【' + str(send_num-error_num-arr_num) + '】')
        logger.info('总计发送错误数量【' + str(error_num) + '】')
        logger.info('成功邮箱账号集合：' + ','.join(send_success_account))
        logger.info('失败邮箱账号集合：' + ','.join(send_failure_account))
        logger.info('脚本结束------------------------------------------------------------------')
        logger.info('')
        # log_file_stream.close()

        j += 1