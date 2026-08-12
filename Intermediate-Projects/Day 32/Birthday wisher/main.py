################ Extra Hard Starting Project ######################

import pandas
import datetime as dt
import random
import smtplib

# 1. Update the birthdays.csv

df = pandas.read_csv("Birthday_wisher/birthdays.csv")

months = df["month"].tolist()
emails = df["email"].tolist()
day = df["day"].tolist()
name = df["name"].tolist()


# 2. Check if today matches a birthday in the birthdays.csv

now = dt.datetime.now()
today_month = now.month
today_date = now.day


def compose_email(name):
    random_number = random.randint(1, 3)

    with open(file=f"Birthday_wisher/letter_templates/letter_{random_number}.txt") as file:
        letter = file.read()

    letter = letter.replace("[NAME]", name)

    return letter


def send_email(email, letter):
    my_email = "your_email.com"
    password = "password"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)

        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"Subject:Birthday Greeting\n\n{letter}"
        )


for no in range(len(emails)):
    if months[no] == today_month and day[no] == today_date:
        letter_edited = compose_email(name[no])
        send_email(
            email=emails[no],
            letter=letter_edited
        )


