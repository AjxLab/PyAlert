# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
import yaml


class PyMailer:
    def __init__(self, address=None, password=None, yaml_file=None):
        ## -----*----- コンストラクタ -----*----- ##
        # address・password / yaml file を指定
        if yaml_file == None:
            # address・passwordを指定
            self.__account = {'address': address, 'password': password}
        else:
            # yaml fileを指定
            self.__account = yaml.load(open(yaml_file), Loader=yaml.SafeLoader)


    def send(self, to_addr, subject, body):
        ## -----*----- メール送信 -----*----- ##
        # メッセージオブジェクトを生成
        msg = self.__create_msg(to_addr, subject, body)

        # 送信
        smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpobj.ehlo()
        smtpobj.starttls()
        smtpobj.ehlo()
        smtpobj.login(self.__account['address'], self.__account['password'])
        smtpobj.sendmail(self.__account['address'], to_addr, msg.as_string())
        smtpobj.close()


    def __create_msg(self, to_addr, subject, body):
        ## -----*----- メッセージを生成 -----*----- ##
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = self.__account['address']
        msg['To'] = to_addr
        msg['Date'] = formatdate()

        return msg


if __name__ == '__main__':
    mailer = PyMailer(yaml_file='gmail.yml')
    mailer.send('abe12@mccc.jp', 'テストタイトル', '夏草や兵どもが夢の跡')
