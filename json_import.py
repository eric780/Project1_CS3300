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
		data[row["Game"]] = {"Game": row["Game"]}
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
	
	(data[gameName])[year] = {"Prize":prize, "Players":players, "Tournaments":tournaments}

for entry in data:
	pprint.pprint(data[entry])
	json.dump(data[entry], jsonfile)