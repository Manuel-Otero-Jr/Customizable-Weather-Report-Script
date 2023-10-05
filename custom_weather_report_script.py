#Importing "random" module for rng
import random

#Variable Settings that are interchangable
TIME_OF_DAY = "afternoon"
REPORTER_NAME = "Al"
SEASON_NAME = ""
CITY_NAME = "New Haven"
currentWeather = ""
DAY_OF_THE_WEEK = "Tuesday"

#Variable Settings NOT to be Changed
weatherNumber = 2
weatherDescriptors = ("cold", "muggy", "hot", "cool")
tempuratureListToUse = [0, 0, 0, 0, 0, 0, 0]
tempList = (random.sample(range(29, 43), 7), random.sample(range(33, 50), 7), random.sample(range(60, 80), 7), random.sample(range(58, 76), 7))
weatherTypes = ("snowy", "rainy", "sunny", "windy")
tempCount = 0

#Small setting up the season #
if SEASON_NAME == "Winter":
    weatherNumber = 0
elif SEASON_NAME == "Spring":
    weatherNumber = 1
elif SEASON_NAME == "Fall" or SEASON_NAME == "Autumn":
    weatherNumber = 3

currentWeather = weatherDescriptors[weatherNumber]
tempuratureListToUse = tempList[weatherNumber]

#Printing the dialogue
print(f"Good {TIME_OF_DAY} everybody, it is a {weatherDescriptors[weatherNumber]} {DAY_OF_THE_WEEK} {TIME_OF_DAY} out here in the city of {CITY_NAME}. I'm {REPORTER_NAME} and I will be your weatherman for today.")
print(f"This week you can expect mostly {weatherTypes[weatherNumber]} weather. Here are the tempurature for this upcoming week!")

#Loading the tempuratures and ending the dialogue
def loadTemps():
    print(f"{tempuratureListToUse[tempCount]}°F")

for tempCount in range(0, 7):
    loadTemps()
else:
    print(f"And that's it for our weather report this {TIME_OF_DAY}.")
    print(f"I'm your weatherman {REPORTER_NAME}, and I hope you have a good {TIME_OF_DAY}!")