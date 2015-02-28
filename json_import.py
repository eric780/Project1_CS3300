import csv
import json
import pprint

csvfile = open("gamesData.csv", 'r')
jsonfile = open("gamesData.json", 'w')

fieldnames = ("Year", "Game", "Prize", "Players", "Tournaments")

reader = csv.DictReader(csvfile, fieldnames)

games = set()
data = dict()

#create dictionaries
for row in reader:
	if row["Game"] not in games:
		data[row["Game"]] = {"Game": row["Game"], "Data": []}
		games.add(row["Game"])

#data is now a dictionary of dictionaries, looks like:
#"Starcraft II": {"Game":"Starcraft II"}

csvfile.seek(0)

for row in reader:
	gameName = row["Game"]
	year = row["Year"]
	prize = row["Prize"]
	players = row["Players"]
	tournaments = row["Tournaments"]
	
	(data[gameName])["Data"].append({"Year": year, "Prize":prize, "Players":players, "Tournaments":tournaments})

datalist = []

for entry in data:
	pprint.pprint(data[entry])
	datalist.append(data[entry])

json.dump(datalist, jsonfile)
#	json.dump(data[entry], jsonfile)
#	jsonfile.write(',')
#	jsonfile.write('\n')