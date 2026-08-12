# 🎂 Birthday Wisher

A Python automation project that automatically sends personalized birthday wishes to people listed in a CSV file.

## 🚀 What This Project Does

The program:

1. Reads birthday information from `birthdays.csv`.
2. Checks today's date.
3. Finds people whose birthday matches today.
4. Selects a random letter template.
5. Replaces `[NAME]` with the person's actual name.
6. Sends the personalized birthday message by email.

## 🛠️ Technologies Used

* Python
* Pandas
* `datetime`
* `random`
* `smtplib`
* CSV files
* Text files
* Gmail SMTP

## 📁 Project Structure

```text
Birthday-Wisher/
├── main.py
├── birthdays.csv
├── requirements.txt
└── letter_templates/
    ├── letter_1.txt
    ├── letter_2.txt
    └── letter_3.txt
```

## 🧠 Python Concepts Practiced

* Pandas DataFrames
* Reading CSV files
* Converting Pandas columns to lists
* File handling
* String `.replace()`
* Random numbers
* Functions
* Loops
* Conditional statements
* `datetime`
* SMTP email automation
* Environment variables / GitHub Secrets

## ⚙️ How It Works

```text
birthdays.csv
      ↓
Read birthday data
      ↓
Get today's date
      ↓
Check for matching birthday
      ↓
Birthday found?
   ↙          ↘
 YES          NO
 ↓             ↓
Choose       Finish
random       program
letter
 ↓
Replace [NAME]
 ↓
Send email 🎉
```

## 📊 Example CSV

```text
name,email,year,month,day
Alex,alex@example.com,2009,8,12
Sam,sam@example.com,2010,5,20
```

## 🔐 Security

Email credentials should **never be stored directly in the Python source code**.

Use environment variables or GitHub Secrets to store the Gmail address and App Password.

## 🤖 Automation

The project can be deployed with **GitHub Actions** so that the Python script runs automatically every day without requiring the local computer to be turned on.

## 🎯 Purpose

This project was created as part of my **100 Days of Python** learning journey to practice data handling, file handling, automation, email communication, and combining multiple Python concepts into a complete application.
