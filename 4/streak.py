import random
flip = []
numberOfStreaks = 0
numberOfStreaksList = []
count = 0
for experimentNumber in range(10000):
    for i in range(0,100):
        if random.randint(0,1) == 0:
            flip.append('H')
        else:
            flip.append('T')

    for i in range (0,100):
        for j in range (i+1,100):
            if flip[i] == flip [j]:
                count += 1
            else:
                count == 0

            if count == 6:
                numberOfStreaks += 1
                count = 0


print('Chance of streak: %s%%' % (numberOfStreaks / (100*10000)))
numberOfStreaksList.append(numberOfStreaks)


