# 5th graders Kara and Rani both have Lemonade stands.
# Kara sells her lemonade at 5 cents a glass and Rani sells hers at 7 cents a glass
# Kara sold 'k' number of glasses of Lemonade today and Rani sold 'r' number of glasses.
# Who made the most money and by what amount?
# 'k' and 'r' are user-entered value.

k = int(input("Enter lemonade for Kara"))
r = int(input("Enter lemonade for Rani"))

totalKara = k*5
totalRani = r*7

def func():
    if totalKara > totalRani:
        return f"Kara made the most money, amount: {totalKara}"
    elif totalKara < totalRani:
        return f"Rani made the most money, amount: {totalRani}"
    elif totalKara == totalRani:
        return f"Kara and Rani made the equal money, amount: {totalRani}"


print(func())