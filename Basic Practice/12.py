# The number of red blood corpuscles in one the cubic millimetre is about 5,000,000
# and the number of white blood corpuscles in one cubix the millimetre is about 8,000.
# What, then is the ratio of white blood corpuscles to red blood Corpuscles?
# Aspect Ratio should be as an int value

# print(5000000/8000)

def greatestCommonFactor (whiteC, redC):
    return whiteC if(redC == 0) else greatestCommonFactor(redC, whiteC % redC)

redCorpuscles = 5000000
whiteCorpuscles = 8000

factor = greatestCommonFactor(whiteCorpuscles, redCorpuscles)

whiteRatio = int(whiteCorpuscles / factor)
redRatio = int(redCorpuscles / factor)

print("Aspect Ratio: ", whiteRatio, ":", redRatio)