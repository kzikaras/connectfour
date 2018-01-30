#connect four


#declare variables and functions
rowOne = ["","","",""]
rowTwo = ["","","",""]
rowThree = ["","","",""]
rowFour = ["","","",""]

def winCheck(rowOne,rowTwo,rowThree,rowFour):
    winner = False
    winningRowOne = ["1","1","1","1"]
    winningRowTwo = ["2","2","2","2"]
    diagonalOne = [rowFour[0],rowThree[1],rowTwo[2],rowOne[3]]
    diagonalTwo = [rowFour[3],rowThree[2],rowTwo[1],rowOne[0]]
    verticalOne = [rowFour[0],rowThree[0],rowTwo[0],rowOne[0]]
    verticalTwo = [rowFour[1],rowThree[1],rowTwo[1],rowOne[1]]
    verticalThree = [rowFour[2],rowThree[2],rowTwo[2],rowOne[2]]
    verticalFour = [rowFour[3],rowThree[3],rowTwo[3],rowOne[3]]
    #check horizontal conditions
    if rowFour == winningRowOne:
        print("Player One wins!")
    elif rowFour == winningRowTwo:
        print("Player Two wins!")
    elif rowThree == winningRowOne:
        print("Player One wins!")
    elif rowThree == winningRowTwo:
        print("Player Two wins!")
    elif rowTwo == winningRowOne:
        print("Player One wins!")
    elif rowTwo == winningRowTwo:
        print("Player Two wins!")
    elif rowOne == winningRowOne:
        print("Player One wins!")
    elif rowOne == winningRowTwo:
        print("Player Two wins!")
    #check vertical conditions
    elif verticalOne == winningRowOne:
      print("Player One wins!")
    elif verticalTwo == winningRowOne:
      print("Player One wins!")
    elif verticalThree == winningRowOne:
      print("Player One wins!")
    elif verticalFour == winningRowOne:
      print("Player One wins!")
    elif verticalOne == winningRowTwo:
      print("Player Two wins!")
    elif verticalTwo == winningRowTwo:
      print("Player Two wins!")
    elif verticalThree == winningRowTwo:
      print("Player Two wins!")
    elif verticalFour == winningRowTwo:
      print("Player Two wins!")
    #Check Diagonal conditions
    elif diagonalOne == winningRowOne or diagonalTwo == winningRowOne:
        print("Player One wins!")
        return winner
    elif diagonalOne == winningRowTwo or diagonalTwo == winningRowTwo:
        print("Player Two wins!")
    


def printBoard(one, two, three, four):
    print(one)
    print(two)
    print(three)
    print(four)



winner = False
print("Welcome to connect four, let's start the game")
while winner == False:
    
    playerChoice = input("Player one choose your row(1, 2, or 3) or press Enter to skip turn: ")
    if playerChoice == "1":
        #if spot is blank, add choice
        if rowFour[0] == "":
            rowFour[0] = "1"
            #if spot is filled, add choice above
        else:
            if rowThree[0] == "":
                rowThree[0] = "1"
            else:
                if rowTwo[0] == "":
                    rowTwo[0] = "1"
                else:
                    if rowOne[0] == "":
                        rowOne[0] = "1"
                    else:
                        print("There is no more room in that column")
           
    elif playerChoice == "2":
        #if spot is blank, add choice
        if rowFour[1] == "":
            rowFour[1] = "1"
            #if spot is filled, add choice above
        else:
            if rowThree[1] == "":
                rowThree[1] = "1"
            else:
                if rowTwo[1] == "":
                    rowTwo[1] = "1"
                else:
                    if rowOne[1] == "":
                        rowOne[1] = "1"
                    else:
                        print("There is no more room in that column")

    elif playerChoice == "3":
        #if spot is blank, add choice
        if rowFour[2] == "":
            rowFour[2] = "1"
            #if spot is filled, add choice above
        else:
            if rowThree[2] == "":
                rowThree[2] = "1"
            else:
                if rowTwo[2] == "":
                    rowTwo[2] = "1"
                else:
                    if rowOne[2] == "":
                        rowOne[2] = "1"
                    else:
                        print("There is no more room in that column")

    elif playerChoice == "4":
        #if spot is blank, add choice
        if rowFour[3] == "":
            rowFour[3] = "1"
            #if spot is filled, add choice above
        else:
            if rowThree[3] == "":
                rowThree[3] = "1"
            else:
                if rowTwo[3] == "":
                    rowTwo[3] = "1"
                else:
                    if rowOne[3] == "":
                        rowOne[3] = "1"
                    else:
                        print("There is no more room in that column")
    
    printBoard(rowOne,rowTwo,rowThree,rowFour)
    winCheck(rowOne,rowTwo,rowThree,rowFour)
    

    playerChoice = input("Player two choose your row(1, 2, or 3) or press Enter to skip turn: ")
    if playerChoice == "1":
        #if spot is blank, add choice
        if rowFour[0] == "":
            rowFour[0] = "2"
            #if spot is filled, add choice above
        else:
            if rowThree[0] == "":
                rowThree[0] = "2"
            else:
                if rowTwo[0] == "":
                    rowTwo[0] = "2"
                else:
                    if rowOne[0] == "":
                        rowOne[0] = "2"
                    else:
                        print("There is no more room in that column")
           
    elif playerChoice == "2":
        #if spot is blank, add choice
        if rowFour[1] == "":
            rowFour[1] = "2"
            #if spot is filled, add choice above
        else:
            if rowThree[1] == "":
                rowThree[1] = "2"
            else:
                if rowTwo[1] == "":
                    rowTwo[1] = "2"
                else:
                    if rowOne[1] == "":
                        rowOne[1] = "2"
                    else:
                        print("There is no more room in that column")

    elif playerChoice == "3":
        #if spot is blank, add choice
        if rowFour[2] == "":
            rowFour[2] = "2"
            #if spot is filled, add choice above
        else:
            if rowThree[2] == "":
                rowThree[2] = "2"
            else:
                if rowTwo[2] == "":
                    rowTwo[2] = "2"
                else:
                    if rowOne[2] == "":
                        rowOne[2] = "2"
                    else:
                        print("There is no more room in that column")

    elif playerChoice == "4":
        #if spot is blank, add choice
        if rowFour[3] == "":
            rowFour[3] = "2"
            #if spot is filled, add choice above
        else:
            if rowThree[3] == "":
                rowThree[3] = "2"
            else:
                if rowTwo[3] == "":
                    rowTwo[3] = "2"
                else:
                    if rowOne[3] == "":
                        rowOne[3] = "2"
                    else:
                        print("There is no more room in that column")
    
    printBoard(rowOne,rowTwo,rowThree,rowFour)
    winCheck(rowOne,rowTwo,rowThree,rowFour)
