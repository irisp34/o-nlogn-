# alternate urls for if you want to specify a state or country code

#api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}
#api.openweathermap.org/data/2.5/weather?q={city name},{state}&appid={your api key}
#api.openweathermap.org/data/2.5/weather?q={city name},{state},
# {country code}&appid={your api key}

"""
NOTE:
# strip punctuation 
# include the case where the person says "today" or "right now" after their 
# sentences 
"""

# Round Half Up Import
import decimal

# Web Scraping Imports
import json
import urllib
from urllib import request


class WeatherAnswers(object):
    # Taken https://www.cs.cmu.edu/~112/
    def __init__(self):
        return
    def roundHalfUp(self, d):
        # Round to nearest with ties going away from zero.
        rounding = decimal.ROUND_HALF_UP
        return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

    def weatherToString(self, text):
        sample = text.split(" ")
        index = sample.index("in")
        city = sample[index+1:]
        city = "+".join(city)
        # Openweathermap is the API we used to gather weather data. 
        # This site gave us information on how to access our weather data:
        # https://openweathermap.org/current
        my_url = f'''http://api.openweathermap.org/data/2.5/weather?q={city}&appid=fea4bf62b107b32ea76781885181c0a0'''
        # TA Ping-Ya helped us with converting the text in my_url to a workable type
        # ig the next two lines 
        htmlText = urllib.request.urlopen(my_url)
        contents = htmlText.readlines()
        contents = contents[0]
        # The next line to convert from bytes to dictionaries came from this site:
        # https://www.geeksforgeeks.org/python-interconversion-between-dictionary-and-bytes/
        dictionaryContents = json.loads(contents.decode('utf-8'))
        return dictionaryContents

    def kelvinToFarenheit(self, kelvin):
        return 32+9/5*(kelvin-273)
    
    def inRange(self, number, two):
        if (number >= two[0]) and (number <= two[1]): return True
        else: return False

    def getWind(self, report, solo):
        windData = report['wind']
        speed = windData['speed']
        angle = windData['deg']
        city = report['name']
        direction = ["north", "east", "south", "west"][self.roundHalfUp(angle/90)%4]
        windNames = [[[8, 12],"gentle breeze"], [[13, 18],"moderate breeze"], [[19, 24],"fresh breeze"],
                     [[25, 31],"strong breeze"], [[32, 46],"gale"], [[47,63],"storm"], [[64,80],"violent storm"]]
        if (speed < 8) and (solo == False): return ""
        elif (speed < 8) and (solo == True):
            return f"It's a calm day in {city}, with a light breeze of {speed} miles per hour moving {direction}."
        else:
            for i in windNames:
                if inRange(speed, i[0]):
                    return f"It's windy today, with a {i[1]} facing {direction}."
            return "Don't venture outside. Find a safe place and hunker down."

    def getWeather(self, report):
        weather = report["weather"][0]
        main = report["main"]
        temperature = self.roundHalfUp(self.kelvinToFarenheit((main['temp'])))
        feelsLike = self.roundHalfUp(self.kelvinToFarenheit((main['feels_like'])))
        city = report['name']
        windInsert = self.getWind(report, False)
        if abs(feelsLike - temperature) < 5:
            weatherString = (f"Right now, the weather in {city} consists of {weather['description']}." + 
                             f' The temperature outside is {temperature} degrees. {windInsert}')
        else:
            weatherString = (f"Right now, the weather in {city} consists of {weather['description']}." + 
                             f' The temperature outside is {temperature} degrees, but it feels like {feelsLike}. {windInsert}')
        return weatherString

    def getHumidity(self, report):
        main = report['main']
        city = report['name']
        humidity = main['humidity']
        return f"The humidity in {city} is currently {humidity} percent."

    def getTemperature(self, report):
        main = report['main']
        city = report['name']
        temp = self.roundHalfUp(self.kelvinToFarenheitmain(main['temp']))
        return f"The temperature in {city} is currently {temp} degrees."

    def DAVIDweather(self,text):
        report = self.weatherToString(text)
        if "weather" in text:
            return self.getWeather(report)
        if "wind speed" in text:
            return self.getWind(report, True)
        if "humidity" in text:
            return self.getHumidity(report)
        if "temperature" in text:
            return self.getTemperature(report)