# 🌧️ Day 35 — Rain Alert

A Python automation project from **Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp**.

This project uses the **OpenWeatherMap API** to check the upcoming weather and the **Twilio API** to send an SMS notification if rain is expected.

---

## 🚀 What This Project Does

The program:

1. Gets weather forecast data from OpenWeatherMap.
2. Checks the weather conditions for the upcoming hours.
3. Looks at the weather condition IDs.
4. Determines whether rain is expected.
5. If rain is expected, sends an SMS alert using Twilio.

### Flow

```text
🌍 Location
     ↓
🌤️ OpenWeatherMap API
     ↓
📊 Weather Forecast
     ↓
🔍 Check Weather IDs
     ↓
☔ Rain expected?
   ↙       ↘
 YES        NO
  ↓          ↓
📱 SMS     ☀️ Done
