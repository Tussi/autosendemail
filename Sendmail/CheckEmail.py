# 检查收件箱是否有退信
import poplib
from datetime import datetime
import re
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr


def checkInbox(em, pas, pop):
    global timediff
    name_list = []
    email = em
    password = pas
    pop3_server = pop
    # 连接到POP3服务器:
    server = poplib.POP3(pop3_server)
    # 可以打开或关闭调试信息:
    server.set_debuglevel(0)
    # 可选:打印POP3服务器的欢迎文字:
    # print(server.getwelcome().decode('utf-8'))

    # 身份认证:
    server.user(email)
    server.pass_(password)

    # stat()返回邮件数量和占用空间:
    # print('Messages: %s. Size: %s' % server.stat())
    # list()返回所有邮件的编号:
    resp, mails, octets = server.list()
    # 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
    # print(mails)

    # 获取最新一封邮件, 注意索引号从1开始:
    index = len(mails)
    # print(index,'2222')
    resp, lines, octets = server.retr(index)

    # lines存储了邮件的原始文本的每一行,
    # 可以获得整个邮件的原始文本:
    msg_content = b'\r\n'.join(lines).decode('utf-8')
    # 稍后解析出邮件:
    msg = Parser().parsestr(msg_content)
    # print(msg)

    messageObject = Parser().parsestr(msg_content)
    msgDate = messageObject["date"]
    # print(678,msgDate)

    # 可以根据邮件索引号直接从服务器删除邮件:
    # server.dele(index)
    # 关闭连接:
    try:
        GMT_FORMAT = '%a, %d %b %Y %H:%M:%S +0800 (CST)'
        new_date = datetime.strptime(msgDate, GMT_FORMAT)
    except:
        GMT_FORMAT = '%a, %d %b %Y %H:%M:%S +0800'
        new_date = datetime.strptime(msgDate, GMT_FORMAT)
    timediff = (datetime.now()-new_date).seconds
    # print("%s秒前"% timediff)
    name_list.append(str(new_date))
    # print(datetime.strptime(msgDate, GMT_FORMAT))
    return timediff

    def print_info(msg, indent=0):

        if indent == 0:
            for header in ['From', 'To', 'Subject']:
                value = msg.get(header, '')
                if value:
                    if header == 'Subject':
                        value = decode_str(value)

                    else:
                        hdr, addr = parseaddr(value)
                        name = decode_str(hdr)
                        value = u'%s <%s>' % (name, addr)

                        print(name)
                print('%s%s: %s' % ('  ' * indent, header, value))
        elif (msg.is_multipart()):
            parts = msg.get_payload()
            for n, part in enumerate(parts):
                print('%spart %s' % ('  ' * indent, n))
                print('%s--------------------' % ('  ' * indent))
                print_info(part, indent + 1)
        else:
            content_type = msg.get_content_type()
            if content_type == 'text/plain' or content_type == 'text/html':
                content = msg.get_payload(decode=True)
                charset = guess_charset(msg)
                if charset:
                    content = content.decode(charset)
                print('%sText: %s' % ('  ' * indent, content + '...'))
        # else:
        #    print('%sAttachment: %s' % ('  ' * indent, content_type))

    def decode_str(s):
        value, charset = decode_header(s)[0]
        if charset:
            value = value.decode(charset)
        return value


    def guess_charset(msg):
        charset = msg.get_charset()
        if charset is None:
            content_type = msg.get('Content-Type', '').lower()
            pos = content_type.find('charset=')
            if pos >= 0:
                charset = content_type[pos + 8:].strip()
        return charset

    print_info(msg=msg)
    print(name_list)

    server.quit()

if __name__ == "__main__":
    e = 'twfqz132vv@126.com'
    p = 'dingzhi60'
    pop = 'pop.126.com'
    checkInbox(e, p, pop)
