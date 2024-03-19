'''
Program used to generate a random draft for the NCAA march madness tourney
Each Participant will have 1 team of each rank, and 4 of each region.
@author Weston Fiala
'''

import random

def randomizedSets():
    '''
    Generates two sets that have no overlap between the indicies
    '''
    lst1 = randomizedSet()
    lst2 = randomizedSet()

    while (lst1[0] == lst2[0]) or (lst1[1] == lst2[1]) or (lst1[2] == lst2[2]) or (lst1[3] == lst2[3]):
        lst2 = randomizedSet()

    return [lst1, lst2]

def randomizedSet():
    '''
    Generates one random set with the values 1-4, with no repeats
    '''
    lst = []

    while lst.__len__() < 4:
        x = random.randint(1, 4)
        if not lst.__contains__(x):
            lst.append(x)
    return lst

# set up the seed for the randomizer
randSeed = 2024
random.seed(randSeed)

done = False

while not done:
    done = False
    secondCheck = False

    temp = []

    # Generate the game matchups. Guaranteed to not have anyone play themselves in the first round.
    for games in range(0, 8):
        temp.append(randomizedSets())

    # Rearrange the list to be sorted by seed instead of game.
    listings = []
    for i in range(0, 8):
        listings.append(temp[i][0])
    for i in range(7, -1, -1):
        listings.append(temp[i][1])

    # Make sure every region has 4 teams from every player.
    playerTally = [0, 0, 0, 0]
    for checker in range(0, 16):
        for level in range(0, 4):
            currentTally = listings[checker][level]
            playerTally[level] = playerTally[level] + (1 << currentTally)
    secondCheck = playerTally[0] == playerTally[1] and playerTally[0] == playerTally[2] and \
            playerTally[0] == playerTally[3]

    # Now we check that no one plays themselves in the second round.
    if secondCheck:
        done = True
        for bracket in range(8, 16):
            for region in range(0,4):
                # Line to check that no player with the 9th - 16th seed team plays themselves in the 2nd round.
                done = done and (listings[bracket][region] != listings[bracket-8][region] or listings[bracket][region] != listings[15-bracket+8][region])

                # Line to check that no player with the 1st - 8th seed team plays themselves in the 2nd round.
                done = done and (listings[15-bracket][region] != listings[bracket-8][region] or listings[15-bracket][region] != listings[15-bracket+8][region])

print(listings)

for listing in listings:
    for rand_assign in listing:
        print(rand_assign)