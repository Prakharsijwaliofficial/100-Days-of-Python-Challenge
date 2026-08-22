import requests
from twilio.rest import Client

# =========================
# CONSTANTS
# =========================

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"

account_sid = "YOUR_TWILIO_ACCOUNT_SID"
auth_token = "YOUR_TWILIO_AUTH_TOKEN"

MY_LAT = YOUR_LATITUDE
MY_LONG = YOUR_LONGITUDE


# =========================
# GET WEATHER DATA
# =========================

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(
    url=OWM_ENDPOINT,
    params=weather_params
)

response.raise_for_status()

weather_data = response.json()


# =========================
# CHECK WEATHER
# =========================

will_rain = False

for hour_data in weather_data["list"]:

    weather_id = hour_data["weather"][0]["id"]

    if weather_id < 700:
        will_rain = True


# =========================
# SEND SMS
# =========================

if will_rain:

    client = Client(
        account_sid,
        auth_token
    )

    message = client.messages.create(
        body="☔ It's going to rain today. Remember to bring an umbrella!",
        from_="YOUR_TWILIO_NUMBER",
        to="YOUR_PHONE_NUMBER"
    )

    print(message.status)

else:

    print("No rain expected. ☀️")
