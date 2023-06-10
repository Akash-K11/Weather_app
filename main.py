import requests as req
import json
import win32com.client as win32com
speaker = win32com.Dispatch("SAPI.SpVoice")
speaker.Speak("Enter the name of city: ")
city = input("Enter the name of city: ")
url1 = f"https://api.weatherapi.com/v1/current.json?key=c7ef015580c64588872204412230806&q={city}"
response1 = req.get(url1)
weather_dict = json.loads(response1.text)
temp_celcius = weather_dict['current']['temp_c']
wind_kph = weather_dict['current']['wind_kph']
humidity = weather_dict['current']['humidity']
output1 = f"In {city}, the temperature is currently {temp_celcius} degree celcius, humidity is {humidity} percent and wind speed is {wind_kph} kilometres per hour."
print(output1)
speaker.Speak(output1)

'''
https://www.weatherapi.com/my/
https://www.weatherapi.com/docs/
https://stackoverflow.com/questions/38540005/how-to-convert-text-to-speech-in-python-3-5-on-windows-10
'''