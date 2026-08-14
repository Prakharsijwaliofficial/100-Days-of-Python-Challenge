# 🚀 ISS Overhead Notifier

A Python automation project from **Day 33 of Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp**.

This project uses APIs to track the **International Space Station (ISS)** and checks whether it is close to my location and whether it is currently dark. If both conditions are true, the program sends an email notification telling me to look up and spot the ISS. 🌌

---

## 📌 Project Overview

The program continuously checks:

1. The current location of the ISS.
2. Whether the ISS is within **±5° latitude and longitude** of my location.
3. The current sunrise and sunset times.
4. Whether it is currently dark.
5. If both conditions are satisfied, an email alert is sent.

The program then waits **60 seconds** and checks again.

---

## 🧠 Concepts Practiced

This project helped me practice:

* 🌐 Working with APIs
* 📡 Making HTTP requests with `requests`
* 📦 Working with JSON data
* 🧭 Latitude and longitude
* 🔢 Converting strings to floats and integers
* 🌅 Sunrise and sunset APIs
* ⏰ Working with `datetime`
* 🔐 SMTP email automation
* 🔄 `while True` loops
* ⏱️ `time.sleep()`
* 🧩 Creating and using functions
* ✅ Boolean conditions
* 🚨 Automated notifications

---

## 🛠️ Technologies Used

* **Python**
* `requests`
* `datetime`
* `smtplib`
* `time`

### APIs Used

* **Open Notify ISS API** — provides the current ISS position.
* **Sunrise-Sunset API** — provides sunrise and sunset times.

---

## 📂 Project Structure

```text
iss-overhead-notifier/
│
└── main.py
```

---

## ⚙️ How It Works

### 1. Get the ISS location

The program requests the current ISS position:

```python
response = requests.get(
    url="http://api.open-notify.org/iss-now.json"
)
```

The latitude and longitude are extracted from the JSON response.

---

### 2. Check whether the ISS is close

The program checks whether the ISS is within **5 degrees** of my latitude and longitude:

```python
if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 \
        and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
```

If it is close, the function returns:

```python
True
```

Otherwise:

```python
False
```

---

### 3. Get sunrise and sunset

The program sends my coordinates to the Sunrise-Sunset API:

```python
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
```

It then extracts the sunrise and sunset hours.

---

### 4. Check if it is dark

The program compares the current hour with sunrise and sunset:

```python
if time_now.hour < sunrise or time_now.hour > sunset:
    return True
```

If it is before sunrise or after sunset, the program considers it dark.

---

### 5. Send an email

If the ISS is close **and** it is dark:

```python
if is_iss_close() and is_dark():
    send_mail()
```

The program connects to Gmail using SMTP:

```python
with smtplib.SMTP("smtp.gmail.com", 587) as connection:
```

Then it sends:

> **Subject:** ISS Alert
> Look up! The ISS is overhead.

---

### 6. Repeat every 60 seconds

The program continuously checks the conditions:

```python
while True:
    ...
    time.sleep(60)
```

This means the program waits 60 seconds between checks.

---

## 📍 My Location

The project currently uses:

* **Latitude:** 29.209503
* **Longitude:** 79.504435
* **Location:** Haldwani, Uttarakhand, India 🇮🇳

These coordinates are used to determine whether the ISS is nearby and to calculate local sunrise and sunset information.

---

## 🔐 Security Note

**Never upload your real Gmail password or App Password to GitHub.**

For the learning version of this project, the code contains placeholders:

```python
my_email = "Your_gmail"
password = "Your_password"
```

For a real deployment, credentials should be stored securely using **environment variables or GitHub Secrets**.

---

## 🚀 Future Improvements

Possible improvements for this project:

* [ ] Use GitHub Actions for automated execution.
* [ ] Store email credentials using GitHub Secrets.
* [ ] Handle India/UTC timezone differences correctly.
* [ ] Prevent duplicate emails during the same ISS pass.
* [ ] Add better error handling for API failures.
* [ ] Create a more precise ISS visibility calculation.
* [ ] Add logging for ISS passes.
* [ ] Create a web dashboard showing the ISS location.

---

## 🎓 Course

**100 Days of Code: The Complete Python Pro Bootcamp**

**Day 33 — API Endpoints & API Parameters**

Project: **ISS Overhead Notifier**

---

## 👨‍💻 Author

**Prakhar Singh Sijwali**

Built as part of my Python learning journey and **100 Days of Code** challenge.

---

⭐ If you found this project interesting, feel free to explore the code and follow the project journey.
