# Write a Python program to takes the user for a distance (in meters)
# and the time was taken (as three numbers: hours, mintues, seconds),
# and display the speed, in miles per hour.

distance = float(input("Distance in meters: "))
hr = float(input("Hours: "))
mint = float(input("Minutes: "))
sec = float(input("Seconds: "))

timeSeconds = (hr * 3600) + (mint * 60) + sec
kph = (distance / 1000) / (timeSeconds / 3600)
mph = kph / 1.609

print("Your speed in miles/h is",mph)