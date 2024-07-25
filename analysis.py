import json

firstMissing = []
secondMissing = []

with open("games_-1.json") as games_json:
    data = json.load(games_json)
    
    count = 0
    for k in data.keys():
        if ("message" in data[k].keys()):
            count += 1
            firstMissing.append(k)


with open("games.json") as games_json:
    data = json.load(games_json)
    
    count = 0
    for k in data.keys():
        if ("message" in data[k].keys()):
            count += 1
            secondMissing.append(k)
            

#print(firstMissing)
#print(secondMissing)

intersection = []
for i in firstMissing:
    if (i in secondMissing):
        intersection.append(i)

print(intersection)
print(len(intersection))