# Mr Richard Tupper is purchasing gifts for his family. So far he has purcahsed the following
# 1) 3 sweaters, each valued at Rs68
# 2) 1 computer game valued at Rs75
# Later, he returned one of the bracelets for a full refund and received a Rs10 rebate on the computer game.
# What is the total cost of the gifts after the refund and rebate?
# Calculation part of the program should be under three lines

# print(68+75+43-10)

sweaterPrice = 68
sweaterCount = 3
computerGamePrice = 75
computerGameCount = 1
braceletPrice = 43
braceletCount = 2

# Discount And Rebate
returnedBraceletCount = 1
rebateOnComputerGame = 10

# Calculate Part
totalGiftPrice = (sweaterPrice * sweaterCount) + (computerGamePrice * computerGameCount) + (braceletPrice * braceletCount)

discountAndRebate = (braceletPrice * returnedBraceletCount) + rebateOnComputerGame

finalGiftPrice = totalGiftPrice - discountAndRebate
print("Final Gift price is ", finalGiftPrice)