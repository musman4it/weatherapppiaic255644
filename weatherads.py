import streamlit as st
import requests
from datetime import datetime

# ➤ 1st Streamlit Command
st.set_page_config(page_title="🌦️ Weather App", layout="centered")

# ➤ App Title
st.title("🌤️ Live Weather & Forecast App  by piaic255664")

# ➤ User input
city_name = st.text_input("Enter city name:")

# ➤ Forecast Function
def get_forecast(lat, lon, api_key):
    forecast_url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "units": "metric"
    }
    forecast_res = requests.get(forecast_url, params=params)

    if forecast_res.status_code == 200:
        return forecast_res.json()
    else:
        return None

# ➤ On button click
if st.button("Check Weather"):

    if city_name == "":
        st.warning("⚠️ Please enter a city name.")
    else:
        api_key = "9c9f81a2b2f560cfb0be068c0ed3cf95"  # Replace with your actual API key

        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city_name,
            "appid": api_key,
            "units": "metric"
        }

        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            data = response.json()

            # ➤ Current Weather Info
            city = data["name"]
            country = data["sys"]["country"]
            temp = data["main"]["temp"]
            description = data["weather"][0]["description"].title()
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            sunrise = datetime.utcfromtimestamp(data["sys"]["sunrise"] + data["timezone"]).strftime('%H:%M:%S')
            sunset = datetime.utcfromtimestamp(data["sys"]["sunset"] + data["timezone"]).strftime('%H:%M:%S')

            # ➤ Weather Icon
            icon_code = data["weather"][0]["icon"]
            icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"

            # ➤ Display Current Weather
            st.success(f"Weather in {city}, {country}")
            st.image(icon_url)
            st.metric(label="🌡️ Temperature", value=f"{temp} °C")
            st.write(f"💧 **Humidity**: {humidity}%")
            st.write(f"🌬️ **Wind Speed**: {wind_speed} m/s")
            st.write(f"🌅 **Sunrise**: {sunrise}")
            st.write(f"🌇 **Sunset**: {sunset}")

            st.snow()

            # ➤ Forecast Section
            lat = data["coord"]["lat"]
            lon = data["coord"]["lon"]

            forecast_data = get_forecast(lat, lon, api_key)

            if forecast_data:
                st.subheader("📅 3-Day Forecast")
                
                # Show every 8th item (every 24 hours in a 3-hour interval forecast)
                for i in range(0, min(24, len(forecast_data["list"])), 8):
                    forecast = forecast_data["list"][i]

                    # Get data from forecast
                    date_txt = forecast["dt_txt"].split(" ")[0]
                    temp = forecast["main"]["temp"]
                    desc = forecast["weather"][0]["description"].title()
                    icon = forecast["weather"][0]["icon"]
                    icon_url = f"http://openweathermap.org/img/wn/{icon}@2x.png"

                    # ➤ Show forecast info
                    st.write(f"### {date_txt}")
                    st.image(icon_url)
                    st.write(f"🌡️ Temp: {temp} °C")
                    st.write(f"☁️ Condition: {desc}")

            else:
                st.warning("No forecast data available.")

        else:
            st.error("City not found. Please try again.")


# Adsterra Direct Link Offer
        adsterra_link = "https://www.effectiveratecpm.com/wt8ijqj84?key=9a748c4acdd52dc0a1dd7616e72d388c"
        st.markdown(f'''
            <a href="{adsterra_link}" target="_blank">
                <button style="background-color: #FF4B4B; color: white; padding: 10px 20px; border-radius: 10px;">
                    🔥 where is cool weather - Click Here!
                </button>
            </a>
        ''', unsafe_allow_html=True)
            
