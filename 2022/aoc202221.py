from sys import stdin
strategyGuide = []


for line in stdin:
    x = line.strip().split(" ")
    strategyGuide.append(x)

def calculate_score(strategyGuide):
    roundScores1 = []
    roundScores2 = []

    for generatedShape, expectedResult in strategyGuide:
        score1 = 0

        if generatedShape == "A":
            generatedChoice = "Rock"
        elif generatedShape == "B":
            generatedChoice = "Paper"
        elif generatedShape == "C":
            generatedChoice = "Scissors"
 
        selectedChoice1 = None
        if expectedResult == "X":
            selectedChoice1 = "Rock"
            score1 += 1
        elif expectedResult == "Y":
            selectedChoice1 = "Paper"
            score1 += 2
        elif expectedResult == "Z":
            selectedChoice1 = "Scissors"
            score1 += 3

        if generatedChoice == selectedChoice1:
            score1 += 3
        elif (generatedChoice == "Rock" and selectedChoice1 == "Paper") or (generatedChoice == "Scissors" and selectedChoice1 == "Rock") or (generatedChoice == "Paper" and selectedChoice1 == "Scissors"):
            score1 += 6

        roundScores1.append(score1) 
        
        selectedChoice2 = None
        score2 = 0
        if expectedResult == "X": # lose
            selectedChoice2 = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}.get(generatedChoice)
        elif expectedResult == "Y": # draw
            selectedChoice2 = generatedChoice
        elif expectedResult == "Z": # win
            selectedChoice2 = {"Rock": "Paper", "Paper": "Scissors", "Scissors": "Rock"}.get(generatedChoice)

        if selectedChoice2 == "Rock":
            score2 += 1
        elif selectedChoice2 == "Paper":
            score2 += 2
        elif selectedChoice2 == "Scissors":
            score2 += 3


        if expectedResult == "Y":
            score2 += 3
        elif expectedResult == "Z":
            score2 += 6
        
        roundScores2.append(score2)

        totalScore1 = sum(roundScores1)
        totalScore2 = sum(roundScores2)

    
    print("Part 1: the total score according to the strategy guide is {}.".format(totalScore1))
    print("Part 2: the total score according to the strategy guide is {}.".format(totalScore2))
    return totalScore1, totalScore2

calculate_score(strategyGuide)
