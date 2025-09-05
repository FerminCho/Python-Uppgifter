import requests
import json

url = "http://football-frenzy.s3-website.eu-north-1.amazonaws.com/list_seasons"
seasons = requests.get(url)


print(seasons.json())

year = input("Enter year: ")
home_score = input("Home score: ")
away_score = input("Away score: ")



