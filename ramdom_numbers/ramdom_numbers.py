import random

print("--------------")
print("Ramdom Numbers")
print("--------------")

userInputFrom = int(input("From? "))
userInputTo = int(input("To? "))

if userInputFrom > userInputTo:
    systemRandomStep = -1

else:
    systemRandomStep = 1

systemRandom = random.randrange(userInputFrom, userInputTo, systemRandomStep)

print(systemRandom)