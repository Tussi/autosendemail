from Sendmail.CheckEmail import checkInbox

a = checkInbox("vx0483@163.com", "gude27", "pop.163.com")
print(a)

# import imaplib
# imapclient = imaplib.IMAP4("imap.126.com", "143")
# imapclient.login('binxibinxi@126.com', 'binxi513021')
# print(imapclient.list())
#
# response, data = imapclient.select('INBOX', False)#针对163邮箱"&XfJT0ZAB-"
# typ, data = imapclient.search(None, 'ALL')
# print(data)
# mail_number = data[0].split()
# print(mail_number)
# for num in mail_number:
#     typ, data = imapclient.fetch(num, '(UID BODY.PEEK[])')
#     if 'OK' != typ:
#         print('fetch mail failed!',num)
#         continue



# -*- coding:UTF-8 -*-
# from imapclient import IMAPClient
# from email.header import decode_header
#
#
# class Imapmail(object):
#
#     def __init__(self):  # 初始化数据
#         self.serveraddress = None
#         self.user = None
#         self.passwd = None
#         self.prot = None
#         self.ssl = None
#         self.timeout = None
#         self.savepath = None
#         self.server = None
#
#     def client(self):  # 链接
#         try:
#             self.server = IMAPClient(self.serveraddress, self.prot, self.ssl, timeout=self.timeout)
#             return self.server
#         except BaseException as e:
#             return "ERROR: >>> " + str(e)
#
#     def login(self):  # 认证
#         try:
#             self.server.login(self.user, self.passwd)
#         except BaseException as e:
#             return "ERROR: >>> " + str(e)
#
#     def getmaildir(self):  # 获取目录列表 [((), b'/', 'INBOX'), ((b'\\Drafts',), b'/', '草稿箱'),]
#         dirlist = self.server.list_folders()
#         # print(dirlist)
#         return dirlist
#
#     def getallmail(self):  # 收取所有邮件
#         print(self.server)
#         self.server.select_folder('已发送', False)  # 选择目录 readonly=True 只读,不修改,这里只选择了 收件箱
#         result = self.server.search()  # 获取所有邮件总数目 [1,2,3,....]
#         print("邮件列表:", result)
#         for _sm in result:
#             # data = self.server.fetch(_sm, ['ENVELOPE'])
#             # size = self.server.fetch(_sm, ['RFC822.SIZE'])
#             # print("大小", size)
#             # envelope = data[_sm][b'ENVELOPE']
#             # print(envelope)
#             # subject = envelope.subject.decode()
#             # if subject:
#             #     subject, de = decode_header(subject)[0]
#             #     subject = subject if not de else subject.decode(de)
#             # dates = envelope.date
#             # print("主题", subject)
#             # print("时间", dates)
#
#             msgdict = self.server.fetch(_sm, ['BODY[]'])  # 获取邮件内容
#             mailbody = msgdict[_sm][b'BODY[]']  # 获取邮件内容
#             # with open(self.savepath + str(_sm), 'wb') as f:  # 存放邮件内容
#             #     f.write(mailbody)
#
#     def close(self):
#         self.server.close()
#
#
# if __name__ == "__main__":
#     imap = Imapmail()
#     imap.serveraddress = "imap.126.com"  # 邮箱地址
#     imap.user = "ajryw3189yl@126.com"  # 邮箱密码
#     imap.passwd = "dingzhi60"  # 邮箱账号
#     imap.savepath = ""  # 邮件存放路径
#     imap.client()
#     imap.login()
#     imap.getmaildir()
#     imap.getallmail()
    # imap.close()
