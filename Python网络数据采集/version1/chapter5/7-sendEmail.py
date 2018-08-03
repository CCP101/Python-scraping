# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

mail_host = "smtp.office365.com"  # 设置服务器
mail_user = "xxxxxxxxxxxxx"  # 用户名
mail_pass = "xxxxxxxxxxxxxx"  # 密码

sender = 'liwentao0523@hotmail.com'
receivers = ['liwentao0523@gmail.com']  # 接收邮件

message = MIMEMultipart()
message['From'] = "xxxxxx<xxxxxxxxxxxxxxxxxxxx>"  # 发送者 称呼<邮件地址>
message['To'] = "xxxx<xxxxxxxxxx>"  # 接收者
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')
message.attach(MIMEText('Send by python & smtplib and email.', 'plain', 'utf-8'))

smtpObj = smtplib.SMTP()
smtpObj.connect(mail_host, 587)  # 587 为 SMTP 端口号
smtpObj.starttls()
# SMTPException("No suitable authentication method found.")
# 抛出异常的地方是上面代码中加粗的地方，主要是当前连接支持server
# 并不支持[AUTH_CRAM_MD5, AUTH_PLAIN, AUTH_LOGIN]
# 中的任何一种认证方式，导致程序运行出现问题。

# 解决方案是：在初始化SMTP和login之间调用starttls()
smtpObj.login(mail_user, mail_pass)
smtpObj.sendmail(sender, receivers, message.as_string())
print("邮件发送成功")


