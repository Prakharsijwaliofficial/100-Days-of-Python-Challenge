
import datetime as dt
import smtplib
import random


with open(file="quotes.txt", mode="r") as file:
    quotes_list = file.readlines()
quote = random.choice(quotes_list)

my_email = "prakharsijwaliofficial@gmail.com"
password = "rcoztdhkoxjcmkcd"
def send_mail():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="jssaerospaceteam@gmail.com",
                            msg= f"Subject:Monday Quotes\n\n{quote}")

now = dt.datetime.now()
week_of_day = now.weekday()

# Monday funtionality
if week_of_day == 2:
    send_mail()
