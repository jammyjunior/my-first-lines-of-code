import random
import sys

print("--------------")
print("Ramdom Numbers")
print("--------------")

userInputFrom = int(input("From? "))
userInputTo = int(input("To? "))

if userInputFrom < userInputTo:
    systemRandomStep = 1

elif userInputFrom > userInputTo:
    systemRandomStep = -1

else:
    print("Error!")
    sys.exit(0)


systemRandom = random.randrange(userInputFrom, userInputTo, systemRandomStep)

print("Your number is", systemRandom)