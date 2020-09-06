# Write a program for a given hour and mintues values calculates an angle in degress
# between the hour and the minutes hands.
# Check whether the minutes hand overlapping the hour at a given time

def calcAngle(h, m):
    if (h < 0 or m < 0 or h > 12 or m > 60 ):
        print("wrong Input")
    
    if h == 12:
        h = 0
    if m == 60:
        m = 0
    hour_anagle = 0.5 * (h*60 + m)
    minute_angle = 6 * m
    angle = abs(hour_anagle - minute_angle)
    angle = min(360 - angle, angle)
    return int(angle)

h = int(input("Enter hour(1 - 12) "))
m = int(input("Enter minute(0 - 59) "))

clockAngle = calcAngle(h, m)
if clockAngle == 0:
    print("Hour and minute hands overlaps")
else:
    print(clockAngle,"degree")
