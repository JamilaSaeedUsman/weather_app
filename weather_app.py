import tkinter as tk
from tkinter import messagebox
import requests

def get_weather(city):
    api_key = '2b35b12b8788c46395ea62f3997564cb'  # my OpenWeatherMap API key
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': api_key}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
 # To make the resquest to the api to get the poarameter i need to pereform my request.

        if response.status_code == 200:
# To check if the request was successful, to make to sure the data of the request meets the stated
# requirment that has been written in the code.

            weather_info = f"Weather in {city}:\n{data['weather'][0]['description']}\nTemperature: {data['main']['temp']}°C"
            messagebox.showinfo('Weather', weather_info)
# To display the information of the request in detailed in a message box.

        else:
            messagebox.showerror('Error', f'Failed to get weather information. Status code: {response.status_code}')
# To display error message if the request wasn't sucessful or if the stated code requirment wasn't met.
    except Exception as e:
        messagebox.showerror('Error', f'An error occurred: {e}')
#  To display error message if an error occured while running the request for instace the sudden
# disconnect from the network.

def get_weather_button_clicked():
    city = city_entry.get()
    if city:
        get_weather(city)
# To retrieve requet in order to print your response.

    else:
        messagebox.showwarning('Warning', 'Please enter a city.')
# It disoplays an error if you don't type in a city.


# GUI setup
app = tk.Tk()
app.title('Weather App')

# Entry for city
city_label = tk.Label(app, text='Enter City:')
city_label.pack(pady=10)

city_entry = tk.Entry(app, width=30)
city_entry.pack(pady=10)

# Button to get weather
get_weather_button = tk.Button(app, text='Get Weather', command=get_weather_button_clicked)
get_weather_button.pack(pady=20)


# Run the app
app.mainloop()

#to start the event loop, which continously listens for and handles user interactions.
#Paddy helps in achieving proper spacing and layout within the GUI App.
    #GUI is the Graphical User Interface, it allows users to interact with a computer or software app.