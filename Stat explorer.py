import requests
import json

year = input("Enter year: ")
if int(year) < 1980 or int(year) > 2018:
    print("ERROR season not in range 1980 - 2018")
    exit()

home_score = input("Home score: ")
away_score = input("Away score: ")#te

url = "http://football-frenzy.s3-website.eu-north-1.amazonaws.com/api/"
season = requests.get(url + str(year)).json()

correct_days = []
for gameday in season["gamedays"]:
    games_data = requests.get(url + str(year) + "/" + str(gameday)).json()
    games_list = games_data["games"]
    for game in games_list:
        if str(game["score"]["home"]["goals"]) == home_score and str(game["score"]["away"]["goals"]) == away_score:
            #correct_days.append(game["date"])
            home_str = " (" + str(game["score"]["home"]["goals"]) + ") " + game["score"]["home"]["team"].split(" ")[0]
            away_str = game["score"]["away"]["team"].split(" ")[0] + " (" + str(game["score"]["away"]["goals"]) + ") "
            print(games_data["date"] + home_str + " - " + away_str)



