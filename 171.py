games = {
    "MLBB": 95,
    "PUBG": 80,
    "Minecraft": 90,
    "Free Fire": 75,
    "Valorant": 85
}

for name in games:
    print(f"{name} : {games[name]}")

print(len(games))

if "Minecraft" in games:
    print("Minecraft Found")

if "GTA" in games:
    print("GTA Found")
else:
    print("GTA Not Found")

games_name = []

for name in games:
    games_name.append(name)

games_name.sort()

print(games_name)

score = []

for name in games:
    score.append(games[name])

score.sort()

print(f"Highest : {score[-1]}")
print(f"Lowest : {score[0]}")