import smtplib

efty=smtplib.SMTP('smtp.gmail.com','587')

efty.ehlo()
efty.starttls()

email=str(input("Enter your Email:"))
pwd=str(input("Enter Your Password:"))
tmail=str(input("Enter Your Target Gmail:"))
msg=str(input("Enter Your Message;"))
amount=int(input("Enter Your Amount:"))

efty.login(email,pwd)

for i in range(amount):
	efty.sendmail(email,tmail,msg)
	