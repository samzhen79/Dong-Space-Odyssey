import json
file = open("leaderboard.txt", "r")

leaderboard_read = file.read().split("\n")

file.close()

leaderboard_list=[]

for item in leaderboard_read[:-1]:
	leaderboard_list.append(json.loads(item))

print(leaderboard_list)