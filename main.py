import requests
import json
import os
from dotenv import load_dotenv, dotenv_values 

load_dotenv()

api_key = os.getenv("SPORTSRADAR_APIKEY")
#url = "https://api.sportradar.com/nfl/official/trial/v7/en/games/88b69b59-d7b9-4572-84d8-6ec00f9af626/statistics.json?api_key=quD73NySmT44z6nsHdaH11fiF9RMNSKz2CqEuqAU"

season2023scheduleURL = f"https://api.sportradar.com/nfl/official/trial/v7/en/games/2023/REG/schedule.json?api_key={api_key}"


headers = {"accept": "application/json"}



response = requests.get(season2023scheduleURL, headers=headers)

missingGames = ['9', '13', '26', '28', '31', '32', '33', '37', '38', '45', '51', '52', '53', '55', '56', '60', '61', '62', '63', '64', '65', '67', '70', '71', '72', '73', '76', '78', '79', '80', '82', '83', '84', '85', '88', '89', '90', '91', '92', '97', '98', '99', '100', '101', '102', '105', '107', '108', '109', '110', '111', '115', '117', '118', '119', '120', '122', '123', '124', '125', '129', '131', '132', '133', '135', '137', '138', '139', '146', '148', '149', '150', '151', '152', '153', '155', '156', '159', '162', '163', '164', '165', '166', '168', '172', '174', '175', '176', '177', '182', '183', '184', '186', '187', '188', '190', '191', '196', '200', '201', '202', '203', '204', '208', '209', '210', '211', '212', '213', '214', '219', '221', '222', '225', '226', '228', '230', '231', '235', '236', '237', '238', '239', '240', '241', '243', '245', '246', '256', '257', '258', '259', '260', '262', '263', '264', '265', '266', '267', '268']

res = response.json()

gameIDs = []

for w in res["weeks"]:
    for g in w["games"]:
        gameIDs.append(g["id"])

games = {}



for i in range(0, len(gameIDs)):
    gameURL = f"https://api.sportradar.com/nfl/official/trial/v7/en/games/{gameIDs[i]}/statistics.json?api_key={api_key}"
    gameRes = requests.get(gameURL, headers=headers)
    gameJSON = gameRes.json()
    games[i] = gameJSON
    print("Just grabbed game ", i)

print("writing....")

with open("games.json", "w") as f:
    json.dump(games, f, ensure_ascii=False, indent=4)


#print(res["statistics"]["home"]["receiving"]["players"])