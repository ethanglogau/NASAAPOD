import requests
import json

my_api_key = "3wafa48C2dr0qASN28zcHCfqvwixdVL6BiJKNiEz"

class APOD:
    
    def getAPODToday():
        query = "https://api.nasa.gov/planetary/apod?api_key={}".format(
            my_api_key
        )
        response = requests.get(
            query,
            headers = {
                "Content-Type": "application/json",
            }
        ) 
        response_json = response.json()
        url = response_json["url"]

        return url

    def getAPODAnyDay(my_date):
        query = "https://api.nasa.gov/planetary/apod?date={}&api_key={}".format(
            my_date,
            my_api_key
        )
        response = requests.get(
            query,
            headers = {
                "Content-Type": "application/json",
            }
        ) 
        response_json = response.json()
        url = response_json["url"]
        explanation = response_json["explanation"]

        return url

print("Today's Astronomy Picture of the Day is given from this URL: ")
my_url_today = APOD.getAPODToday()
print(my_url_today)

my_date = input("Input a date for an APOD in the format YYYY-MM-DD: ")
my_url_any_day = APOD.getAPODAnyDay(my_date)
print(my_url_any_day)

