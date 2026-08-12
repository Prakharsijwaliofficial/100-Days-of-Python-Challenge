# 📩 Monday Quotes Emailer

A Python automation project that sends a random motivational quote by email every Monday.

## 🚀 What This Project Does

The program:

1. Reads motivational quotes from a `quotes.txt` file.
2. Selects a random quote.
3. Checks the current day of the week.
4. If it is Monday, sends the quote through Gmail using SMTP.

## 🛠️ Technologies Used

* Python
* `datetime`
* `random`
* `smtplib`
* File Handling
* Gmail SMTP

## 📁 Project Structure

```text
Monday-Quotes/
├── main.py
└── quotes.txt
```

## 🧠 Python Concepts Practiced

* Reading `.txt` files
* Lists
* `random.choice()`
* Functions
* `datetime`
* `weekday()`
* Conditional statements
* SMTP email automation
* Environment variables / secrets

## ⚙️ How It Works

```text
quotes.txt
     ↓
Read quotes
     ↓
Choose random quote
     ↓
Check today's day
     ↓
Is it Monday?
   ↙       ↘
 YES       NO
 ↓          ↓
Send       Stop
email
```

## 🔐 Security

Email credentials should **never be hardcoded** in the source code.

Use environment variables or GitHub Secrets for the Gmail address and App Password.

## 🎯 Purpose

This project was created as part of my **100 Days of Python** learning journey to practice file handling, automation, functions, dates, and email communication with Python.
