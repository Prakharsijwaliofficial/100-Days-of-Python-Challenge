# 📊 Day 37 — Habit Tracker with Pixela API

A Python habit-tracking project built as part of the **100 Days of Code: The Complete Python Pro Bootcamp by Angela Yu**.

This project introduced me to working with **REST APIs**, sending HTTP requests with Python, handling JSON data, authentication headers, and using API endpoints to create and manage a habit-tracking graph.

---

## 🚀 What This Project Does

The project uses the **Pixela API** to create and manage a visual habit/activity graph.

It can:

- 👤 Create a Pixela user
- 📈 Create a graph
- ➕ Add a pixel to the graph
- ✏️ Update an existing pixel
- 🗑️ Delete a pixel
- 📅 Work with dates using Python's `datetime`
- 🔐 Keep API credentials outside the source code using environment variables

---

## 🧠 How It Works

```text
Python Program
      │
      ▼
   Pixela API
      │
      ├── Create User
      │
      ├── Create Graph
      │
      ├── Add Pixel
      │
      ├── Update Pixel
      │
      └── Delete Pixel
