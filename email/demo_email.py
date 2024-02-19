import smtplib
from email.mime.text import MIMEText
from email.header import Header

smtpObj = smtplib.SMTP(host="smtp.163.com", port=25)


sender = ""
senderPwd = ""

receivers = [""]

content = MIMEText("测试发送", "plain", "utf-8")

from_str = f"测试From<{sender}>"
content["From"] = from_str
content["To"] = Header("测试To", "utf-8")
content["Subject"] = Header("标题", "utf-8")

smtpObj.login(sender, senderPwd)
smtpObj.sendmail(sender, receivers, content.as_string())
smtpObj.close()
print("发送成功")