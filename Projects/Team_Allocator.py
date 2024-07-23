import random

players = ["Ram", "Shyam", "Balram", "Laxman", "Radhe", "Rajni"]

print("~ ~ ~ Welcome to Team Allocator ~ ~ ~")

random.shuffle(players)
team1 = players[:len(players)//2]
cap1 = random.choice(team1)

team2 = players[len(players)//2:]
cap2 = random.choice(team2)

print("Team 1 : ")
print("Caption : " + cap1)
for players in team1:
    print(players)


print("Team 2 : ")
print("Caption  : " + cap2)
for players in team2:
    print(players)