import requests

url = "https://weathercast-arduino.herokuapp.com/saveArduino"

data = {
    "api_key": "ArduinoApiKey@00191CA7",
    "data": ["12345", "98756", "879654", "565656", "111111", "222222"]
}

x = requests.post(url, data = data)

print(x.text)