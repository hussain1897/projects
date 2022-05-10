import requests

API_KEY = "d39416efcabadcd1b3d299f8eed3786b"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name : ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
#have base url, pass on api key quiery parameter, & for second parameter, 
# q for next quiery,city is next parameter  
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print(weather)
    temperature = round(data["main"]["temp"] -273.15)
    print("weather:", weather)
    print("Temperature:", temperature, "celsius")
else:
    print("An error occured.")