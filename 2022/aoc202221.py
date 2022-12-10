strategyGuide = []

while True:

    inp = ""
    try:
        inp = input()

    except EOFError:
        break

    x = inp.split(" ")
    strategyGuide.append(x)

roundScores1 = [] 
roundScores2 = []

def scoreCalculator(strategyGuide):
    iterator = 0
    score = 0
    while iterator < len(strategyGuide):
        generatedShape = strategyGuide[iterator][0]
        if generatedShape == "A":
            generatedChoice = "Rock" 
        elif generatedShape == "B":
            generatedChoice = "Paper" 
        elif generatedShape == "C":
            generatedChoice = "Scissors" 


        selectedShape = strategyGuide[iterator][1]
        if selectedShape == "X":
            selectedChoice = "Rock" 
            score += 1
        elif selectedShape == "Y":
            selectedChoice = "Paper"
            score += 2
        elif selectedShape == "Z":
            selectedChoice = "Scissors"
            score +=3

        if generatedChoice == selectedChoice:
            result = "Draw"
        elif (generatedChoice == "Rock") and (selectedChoice == "Paper"):
            result = "Win"
        elif (generatedChoice == "Paper") and (selectedChoice == "Scissors"):
            result = "Win"
        elif (generatedChoice == "Scissors") and (selectedChoice == "Rock"):
            result = "Win"
        else: 
            result = "Lose"

        if result == "Draw":
            score += 3
        elif result == "Win":
            score += 6
        
        
        roundScores1.append(score)
        score = 0
        iterator += 1


def part2(strategyGuide):
    iterator = 0
    score = 0
    while iterator < len(strategyGuide):
        generatedShape = strategyGuide[iterator][0]
        if generatedShape == "A":
            generatedChoice = "Rock" 
        elif generatedShape == "B":
            generatedChoice = "Paper" 
        elif generatedShape == "C":
            generatedChoice = "Scissors" 


        expectedResult = strategyGuide[iterator][1]
        if expectedResult == "X": #lose
            result = "Lose" 
            if generatedChoice == "Rock":
                selectedChoice = "Scissors"
            elif generatedChoice == "Paper":
                selectedChoice = "Rock"
            elif generatedChoice == "Scissors":
                selectedChoice = "Paper"

        elif expectedResult == "Y": #draw
            result = "Draw"
            selectedChoice = generatedChoice
        elif expectedResult == "Z": #win
            result = "Win"
            if generatedChoice == "Rock":
                selectedChoice = "Paper"
            elif generatedChoice == "Paper":
                selectedChoice = "Scissors"
            elif generatedChoice == "Scissors":
                selectedChoice = "Rock"
        
        if selectedChoice == "Rock":
            score += 1
        elif selectedChoice == "Paper":
            score += 2
        elif selectedChoice == "Scissors":
            score += 3
    

        if result == "Draw":
            score += 3
        elif result == "Win":
            score += 6
        
        
        roundScores2.append(score)
        score = 0
        iterator += 1


scoreCalculator(strategyGuide)
part2(strategyGuide)
totalScore1 = sum(roundScores1)
totalScore2 = sum(roundScores2)
print("Answer for Day 1 is: ", totalScore1)
print("Answer for Day 2 is: ", totalScore2)

