import tkinter as tk
import requests

def get_weather():
    city = city_entry.get()
    api_key = "your_openweather_api_key"  # Replace with your API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        result_label.config(text=f"Temp: {temp}°C\nDescription: {description}")
    else:
        result_label.config(text="City not found!")

root = tk.Tk()
root.title("Weather App")

city_entry = tk.Entry(root, width=30)
city_entry.pack()

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
