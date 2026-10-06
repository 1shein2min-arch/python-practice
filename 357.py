import json

try :
    with open("repair.json","r") as file :
        repairs = json.load(file)
except FileNotFoundError :
    repairs = []

except json.JSONDecodeError :
    repairs = []
print(repairs)