# Salesperson Rita drives 2,052 miles in 6 days, stopping at 2 towns each day.
# How many kilometers does she average betweeen stops?

totalMilesToDrive = 2052
totalDays = 6
townToStopPerDay = 2
kmPerMile = 1.60934

avgMiles = (totalMilesToDrive / totalDays) / townToStopPerDay
# Convert miles to Km
avgKM = avgMiles * kmPerMile
print("She drive average of ", avgKM,"km between every stop")

# --------OR---------


def get(x, y, z):
    eachdayDistance = x/y
    eachTownDistanceInMiles = eachdayDistance/z
    return eachTownDistanceInMiles*1.60934
    
totalDistance = 2052
totalDays = 6
townStop = 2
print(get(totalDistance, totalDays, townStop),'Km')