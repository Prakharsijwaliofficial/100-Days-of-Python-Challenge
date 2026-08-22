# 📈 Day 36 — Stock Trading News Alert

A Python automation project from **Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp**.

This project monitors a company's stock price and automatically searches for related news when the stock experiences a significant price movement. It then sends the top news articles to a verified phone number using Twilio.

---

## 🚀 What This Project Does

The program monitors **Tesla (TSLA)**.

It:

1. Gets Tesla's daily stock data from Alpha Vantage.
2. Finds yesterday's closing price.
3. Finds the previous trading day's closing price.
4. Calculates the price difference.
5. Determines whether the stock went up 🔺 or down 🔻.
6. Calculates the percentage change.
7. If the movement is significant, searches NewsAPI for Tesla-related news.
8. Takes the first 3 articles.
9. Uses list comprehension to format the articles.
10. Sends each article as a separate SMS using Twilio.

---

## 🔄 Project Flow

```text
                 Tesla (TSLA)
                      │
                      ▼
             📊 Alpha Vantage
                      │
                      ▼
          Yesterday's Closing Price
                      │
                      ▼
       Previous Trading Day's Price
                      │
                      ▼
             Calculate Difference
                      │
                      ▼
             Calculate Percentage
                      │
                      ▼
             Significant Movement?
                /           \
              YES            NO
               │              │
               ▼              ▼
          📰 NewsAPI         Finish
               │
               ▼
          First 3 Articles
               │
               ▼
       List Comprehension
               │
               ▼
          📱 Twilio SMS
