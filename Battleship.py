from random import randint
import time
import os
letters = ["XX","A","B","C","D","E","F","G","H","I","J"]
dev = 1
lastHit = 0

'''
PLAYER INITIALIZATION
'''

def Carrier(playerBoard,playerShips):
    newPlayerBoard = [playerBoard[i].copy() for i in range(0,11)]
    newPlayerShips = playerShips.copy()
    Carrier = []
    print("Placing Carrier (5 Spaces): ")
    print("Choose orientation:")
    print("1. Place ship from left coordinate to right coordinate")
    print("2. Place ship from bottom coordinate to top coordinate")
    orient = input("Enter choice(1-2): ")
    if orient == "1" or orient == "2":
        pass
    else:
        print("Invalid choice! Try again! ")
        return 0

    start = input("Enter start coordinate (in B4 format): ")
    if start[0] in letters:
        try:
            if 0 < int(start[1:]) < 11:
                pass
            else:
                print("Invalid coordinate! Try again!")
                return 0
        except:
            print("Invalid coordinate! Try again! ")
            return 0
    else:
        print("Invalid coordinate! Try again! ")
        return 0

    letter = start[0]
    num = int(start[1:])
    letternum = int(letters.index(letter))

    try: 
        if int(orient) == 1:
            for i in range(5):
                if newPlayerBoard[num][letternum+i] == "-":
                    newPlayerBoard[num][letternum+i] = "X"
                    Carrier.append(letters[letternum+i]+str(num))
                else:
                    print("Selected coordinate makes boat go out of map! Try again! ")
                    return 0
        elif int(orient) == 2:
            for i in range(5):
                if newPlayerBoard[num-i][letternum] == "-":
                    newPlayerBoard[num-i][letternum] = "X"
                    Carrier.append(letters[letternum]+str(num-i))
                else:
                    print("Selected coordinate makes boat go out of map! Try again! ")
                    return 0
        else: 
            print("Invalid choice! Try again! ")
            return 0
        
    except ValueError:
        print("Invalid input! Try again! ")
        return 0
    
    except IndexError:
        print("Selected coordinate makes boat go out of map! Try again! ")
        return 0
    
    newPlayerShips["Carrier"] = Carrier 
    return [newPlayerBoard,newPlayerShips]
    
def Battleship(playerBoard,playerShips):
    newPlayerBoard = [playerBoard[i].copy() for i in range(0,11)]
    newPlayerShips = playerShips.copy()
    Battleship = []
    print("Placing Battleship (4 Spaces): ")
    print("Choose orientation:")
    print("1. Place ship from left coordinate to right coordinate")
    print("2. Place ship from bottom coordinate to top coordinate")
    orient = input("Enter choice(1-2): ")
    if orient == "1" or orient == "2":
        pass
    else:
        print("Invalid choice! Try again! ")
        return 0

    start = input("Enter start coordinate (in B4 format): ")
    if start[0] in letters:
        try:
            if 0 < int(start[1:]) < 11:
                pass
            else:
                print("Invalid coordinate! Try again!")
                return 0
        except:
            print("Invalid coordinate! Try again! ")
            return 0
    else:
        print("Invalid coordinate! Try again! ")
        return 0

    letter = start[0]
    num = int(start[1:])
    letternum = int(letters.index(letter))

    try: 
        if int(orient) == 1:
            for i in range(4):
                if newPlayerBoard[num][letternum+i] == "-":
                    newPlayerBoard[num][letternum+i] = "X"
                    Battleship.append(letters[letternum+i]+str(num))
                elif newPlayerBoard[num][letternum+i] == "X":
                    print("Selected coordinate already has a boat! Try again! ")
                    return 0
                else:
                    print("Selected coordinate makes boat go out of map! Try again! ")
                    return 0

        elif int(orient) == 2:
            for i in range(4):
                if newPlayerBoard[num-i][letternum] == "-":
                    newPlayerBoard[num-i][letternum] = "X"
                    Battleship.append(letters[letternum]+str(num-i))
                elif newPlayerBoard[num-i][letternum] == "X":
                    print("Selected coordinate already has a boat! Try again! ")
                    return 0
                else:
                    print("Selected coordinate makes boat go out of map! Try again! ")
                    return 0
        else: 
            print("Invalid choice! Try again! ")
            return 0
    
    except IndexError:
        print("Selected coordinate makes boat go out of map! Try again! ")
        return 0
    
    except ValueError:
        print("Invalid input! Try again!")
        return 0
    
    newPlayerShips["Battleship"] = Battleship 
    return [newPlayerBoard,newPlayerShips]
    
def Destroyer(playerBoard,playerShips):
    newPlayerBoard = [playerBoard[i].copy() for i in range(0,11)]
    newPlayerShips = playerShips.copy()
    Destroyer = []
    print("Placing Destroyer (3 Spaces): ")
    print("Choose orientation:")
    print("1. Place ship from left coordinate to right coordinate")
    print("2. Place ship from bottom coordinate to top coordinate")
    orient = input("Enter choice(1-2): ")
    if orient == "1" or orient == "2":
        pass
    else:
        print("Invalid choice! Try again! ")
        return 0

    start = input("Enter start coordinate (in B4 format): ")
    if start[0] in letters:
        try:
            if 0 < int(start[1:]) < 11:
                pass
            else:
                print("Invalid coordinate! Try again!")
                return 0
        except:
            print("Invalid coordinate! Try again! ")
            return 0
    else:
        print("Invalid coordinate! Try again! ")
        return 0

    letter = start[0]
    num = int(start[1:])
    letternum = int(letters.index(letter))

    try: 
        if int(orient) == 1:
            for i in range(3):
                if newPlayerBoard[num][letternum+i] == "-":
                    newPlayerBoard[num][letternum+i] = "X"
                    Destroyer.append(letters[letternum+i]+str(num))
                elif newPlayerBoard[num][letternum+i] == "X":
                    print("Selected coordinate already has a boat! Try again! ")
                    return 0
                else:
                    print("Selected coordinate makes boat go out of map! Try again! ")
                    return 0

        elif int(orient) == 2:
            for i in range(3):
                if newPlayerBoard[num-i][letternum] == "-":
                    newPlayerBoard[num-i][letternum] = "X"
                    Destroyer.append(letters[letternum]+str(num-i))
                elif newPlayerBoard[num-i][letternum] == "X":
                    print("Selected coordinate already has a boat! Try again! ")
                    return 0
                else:
                    print("Selected coordinate makes boat go out of map! Try again! ")
                    return 0
        else: 
            print("Invalid choice! Try again! ")
            return 0
    
    except IndexError:
        print("Selected coordinate makes boat go out of map! Try again! ")
        return 0
    
    except ValueError:
        print("Invalid input! Try again!")
        return 0
    
    newPlayerShips["Destroyer"] = Destroyer 
    return [newPlayerBoard, newPlayerShips]

def Submarine(playerBoard,playerShips):
    newPlayerBoard = [playerBoard[i].copy() for i in range(0,11)]
    newPlayerShips = playerShips.copy()
    Submarine = []
    print("Placing Submarine (3 Spaces): ")
    print("Choose orientation:")
    print("1. Place ship from left coordinate to right coordinate")
    print("2. Place ship from bottom coordinate to top coordinate")
    orient = input("Enter choice(1-2): ")
    if orient == "1" or orient == "2":
        pass
    else:
        print("Invalid choice! Try again! ")
        return 0

    start = input("Enter start coordinate (in B4 format): ")
    if start[0] in letters:
        try:
            if 0 < int(start[1:]) < 11:
                pass
            else:
                print("Invalid coordinate! Try again!")
                return 0
        except:
            print("Invalid coordinate! Try again! ")
            return 0
    else:
        print("Invalid coordinate! Try again! ")
        return 0

    letter = start[0]
    num = int(start[1:])
    letternum = int(letters.index(letter))

    try: 
        if int(orient) == 1:
            for i in range(3):
                if newPlayerBoard[num][letternum+i] == "-":
                    newPlayerBoard[num][letternum+i] = "X"
                    Submarine.append(letters[letternum+i]+str(num))
                elif newPlayerBoard[num][letternum+i] == "X":
                    print("Selected coordinate already has a boat! Try again! ")
                    return 0
                else:
                    print("Selected coordinate makes boat go out of map! Try again! ")
                    return 0

        elif int(orient) == 2:
            for i in range(3):
                if newPlayerBoard[num-i][letternum] == "-":
                    newPlayerBoard[num-i][letternum] = "X"
                    Submarine.append(letters[letternum]+str(num-i))
                elif newPlayerBoard[num-i][letternum] == "X":
                    print("Selected coordinate already has a boat! Try again! ")
                    return 0
                else:
                    print("Selected coordinate makes boat go out of map! Try again! ")
                    return 0
        else: 
            print("Invalid choice! Try again! ")
            return 0
    
    except IndexError:
        print("Selected coordinate makes boat go out of map! Try again! ")
        return 0
    
    except ValueError:
        print("Invalid input! Try again!")
        return 0
    
    newPlayerShips["Submarine"] = Submarine 
    return [newPlayerBoard,newPlayerShips]

def PatrolBoat(playerBoard,playerShips):
    newPlayerBoard = [playerBoard[i].copy() for i in range(0,11)]
    newPlayerShips = playerShips.copy()
    PatrolBoat = []
    print("Placing Patrol Boat (2 Spaces): ")
    print("Choose orientation:")
    print("1. Place ship from left coordinate to right coordinate")
    print("2. Place ship from bottom coordinate to top coordinate")
    orient = input("Enter choice(1-2): ")
    if orient == "1" or orient == "2":
        pass
    else:
        print("Invalid choice! Try again! ")
        return 0 

    start = input("Enter start coordinate (in B4 format): ")
    if start[0] in letters:
        try:
            if 0 < int(start[1:]) < 11:
                pass
            else:
                print("Invalid coordinate! Try again!")
                return 0
        except:
            print("Invalid coordinate! Try again! ")
            return 0
    else:
        print("Invalid coordinate! Try again! ")
        return 0

    letter = start[0]
    num = int(start[1:])
    letternum = int(letters.index(letter))

    try: 
        if int(orient) == 1:
            for i in range(2):
                if newPlayerBoard[num][letternum+i] == "-":
                    newPlayerBoard[num][letternum+i] = "X"
                    PatrolBoat.append(letters[letternum+i]+str(num))
                elif newPlayerBoard[num-i][letternum] == "X":
                    print("Selected coordinate already has a boat! Try again! ")
                    return 0
                else:
                    print("Selected coordinate makes boat go out of map! Try again! ")
                    return 0

        elif int(orient) == 2:
            for i in range(2):
                if newPlayerBoard[num-i][letternum] == "-":
                    newPlayerBoard[num-i][letternum] = "X"
                    PatrolBoat.append(letters[letternum]+str(num-i))
                elif newPlayerBoard[num-i][letternum] == "X":
                    print("Selected coordinate already has a boat! Try again! ")
                    return 0
                else:
                    print("Selected coordinate makes boat go out of map! Try again! ")
                    return 0
        else: 
            print("Invalid choice! Try again! ")
            return 0
    
    except IndexError:
        print("Selected coordinate makes boat go out of map! Try again! ")
        return 0
    
    except ValueError:
        print("Invalid input! Try again!")
        return 0
    
    newPlayerShips["PatrolBoat"] = PatrolBoat
    return [newPlayerBoard, newPlayerShips]

def playerInit(playerBoard,playerShips):
    print("The starting grid is as follows: ")
    for i in playerBoard:
        for j in i: 
            print(j,end=" ")
        print()
    print()
    
    params = Carrier(playerBoard,playerShips)
    while params == 0:
        print()
        params = Carrier(playerBoard,playerShips)
    playerBoard = params[0]
    playerShips = params[1]
    
    print("\n\t************************")
    print("\tGrid after placement:")
    for i in playerBoard:
        for j in i: 
            print(j,end=" ")
        print()
    print()
    
    params = Battleship(playerBoard,playerShips)
    while params == 0:
        print()
        params = Battleship(playerBoard,playerShips)
    playerBoard = params[0]
    playerShips = params[1]
    
    print("\n\t************************")
    print("\tGrid after placement:")
    for i in playerBoard:
        for j in i: 
            print(j,end=" ")
        print()
    print()

    params = Destroyer(playerBoard,playerShips)
    while params == 0:
        print()
        params = Destroyer(playerBoard,playerShips)
    playerBoard = params[0]
    playerShips = params[1]
    
    print("\n\t************************")
    print("\tGrid after placement:")
    for i in playerBoard:
        for j in i: 
            print(j,end=" ")
        print()
    print()
    
    params = Submarine(playerBoard,playerShips)
    while params == 0:
        print()
        params = Submarine(playerBoard,playerShips)
    playerBoard = params[0]
    playerShips = params[1]

    print("\n\t************************")
    print("\tGrid after placement:")
    for i in playerBoard:
        for j in i: 
            print(j,end=" ")
        print()
    print()
    
    params = PatrolBoat(playerBoard,playerShips)
    while params == 0:
        print()
        params = PatrolBoat(playerBoard,playerShips)
    playerBoard = params[0]
    playerShips = params[1]
    
    print("\n\t************************")
    print("\tGrid after placement:")
    for i in playerBoard:
        for j in i: 
            print(j,end=" ")
        print()
    print()

    return [playerBoard,playerShips]

'''
PLAYER TURN
'''
 
def playerTurn(attackingPlayerAttempts,defendingShips):
    try:
        num = int(input("Enter row number(1-10): "))
        if num > 10 or num < 1:
            print("Invalid coordinate entered! Try again...")
            return 1 
        letter = input("Enter column letter(A-J): ").upper()
        if letter in letters: 
            letternum = int(letters.index(letter))
        else:
            print("Invalid coordinate entered! Try again...")
            return 1
        coord = letter+str(num)
    except:
        print("Invalid coordinate entered! Try again...")
        return 1

    if coord in defendingShips["Carrier"]:
        attackingPlayerAttempts[num][letternum] = "H"
        print("A HIT!")
        defendingShips["Carrier"].remove(coord)
        if len(defendingShips["Carrier"]) == 0:
            print("Carrier has sunk! ")

    elif coord in defendingShips["Battleship"]:
        attackingPlayerAttempts[num][letternum] = "H"
        print("A HIT!")
        defendingShips["Battleship"].remove(coord)
        if len(defendingShips["Battleship"]) == 0:
            print("Battleship has sunk! ")

    elif coord in defendingShips["Destroyer"]:
        attackingPlayerAttempts[num][letternum] = "H"
        print("A HIT!")
        defendingShips["Destroyer"].remove(coord)
        if len(defendingShips["Destroyer"]) == 0:
            print("Destroyer has sunk! ")

    elif coord in defendingShips["Submarine"]:
        attackingPlayerAttempts[num][letternum] = "H"
        print("A HIT!")
        defendingShips["Submarine"].remove(coord)
        if len(defendingShips["Submarine"]) == 0:
            print("Submarine has sunk! ")

    elif coord in defendingShips["PatrolBoat"]:
        attackingPlayerAttempts[num][letternum] = "H"
        print("A HIT!")
        defendingShips["PatrolBoat"].remove(coord)
        if len(defendingShips["PatrolBoat"]) == 0:
            print("Patrol Boat has sunk! ")
    else:
        if attackingPlayerAttempts[num][letternum] == "H" or attackingPlayerAttempts[num][letternum] == "M":
            print("Coordinate was already tried! Try again...")
            return 1
        else:
            attackingPlayerAttempts[num][letternum] = "M"
            print("A MISS!")
    
    return 0

'''
COMPUTER INITIALIZATION
'''

def cCarrier(computerBoard,computerShips):
    newComputerBoard = [computerBoard[i].copy() for i in range(0,11)]
    newComputerShips = computerShips.copy()
    Carrier = []
    orient = randint(1,2)

    num = randint(1,10)
    letternum = randint(1,10)

    try: 
        if int(orient) == 1:
            for i in range(5):
                if newComputerBoard[num][letternum+i] == "-":
                    newComputerBoard[num][letternum+i] = "X"
                    Carrier.append(letters[letternum+i]+str(num))
                else:
                    return 0
        elif int(orient) == 2:
            for i in range(5):
                if newComputerBoard[num][letternum+i] == "-":
                    newComputerBoard[num-i][letternum] = "X"
                    Carrier.append(letters[letternum]+str(num-i))
                else:
                    return 0
        else: 
            return 0
        
    except ValueError:
        return 0
    
    except IndexError:
        return 0
    
    newComputerShips["Carrier"] = Carrier 
    return [newComputerBoard, newComputerShips]
    
def cBattleship(computerBoard,computerShips):
    newComputerBoard = [computerBoard[i].copy() for i in range(0,11)]
    newComputerShips = computerShips.copy()
    Battleship = []
    orient = randint(1,2)

    num = randint(1,10)
    letternum = randint(1,10)

    try: 
        if int(orient) == 1:
            for i in range(4):
                if newComputerBoard[num][letternum+i] == "-":
                    newComputerBoard[num][letternum+i] = "X"
                    Battleship.append(letters[letternum+i]+str(num))
                else:
                    return 0

        elif int(orient) == 2:
            for i in range(4):
                if newComputerBoard[num-i][letternum] == "-":
                    newComputerBoard[num-i][letternum] = "X"
                    Battleship.append(letters[letternum]+str(num-i))
                else:
                    return 0
        else: 
            return 0
    
    except IndexError:
        return 0
    
    except ValueError:
        return 0
    
    newComputerShips["Battleship"] = Battleship 
    return [newComputerBoard,newComputerShips]
    
def cDestroyer(computerBoard,computerShips):
    newComputerBoard = [computerBoard[i].copy() for i in range(0,11)]
    newComputerShips = computerShips.copy()
    Destroyer = []
    orient = randint(1,2)

    num = randint(1,10)
    letternum = randint(1,10)
    try: 
        if int(orient) == 1:
            for i in range(3):
                if newComputerBoard[num][letternum+i] == "-":
                    newComputerBoard[num][letternum+i] = "X"
                    Destroyer.append(letters[letternum+i]+str(num))
                else:
                    return 0

        elif int(orient) == 2:
            for i in range(3):
                if newComputerBoard[num-i][letternum] == "-":
                    newComputerBoard[num-i][letternum] = "X"
                    Destroyer.append(letters[letternum]+str(num-i))
                else:
                    return 0
        else: 
            return 0
    
    except IndexError:
        return 0
    
    except ValueError:
        return 0
    
    newComputerShips["Destroyer"] = Destroyer 
    return [newComputerBoard,newComputerShips]

def cSubmarine(computerBoard,computerShips):
    newComputerBoard = [computerBoard[i].copy() for i in range(0,11)]
    newComputerShips = computerShips.copy()
    Submarine = []
    orient = randint(1,2)

    num = randint(1,10)
    letternum = randint(1,10)

    try: 
        if int(orient) == 1:
            for i in range(3):
                if newComputerBoard[num][letternum+i] == "-":
                    newComputerBoard[num][letternum+i] = "X"
                    Submarine.append(letters[letternum+i]+str(num))
                else:
                    return 0

        elif int(orient) == 2:
            for i in range(3):
                if newComputerBoard[num-i][letternum] == "-":
                    newComputerBoard[num-i][letternum] = "X"
                    Submarine.append(letters[letternum]+str(num-i))
                else:
                    return 0
        else: 
            return 0
    
    except IndexError:
        return 0
    
    except ValueError:
        return 0
    
    newComputerShips["Submarine"] = Submarine 
    return [newComputerBoard,newComputerShips]

def cPatrolBoat(computerBoard,computerShips):
    newComputerBoard = [computerBoard[i].copy() for i in range(0,11)]
    newComputerShips = computerShips.copy()  
    PatrolBoat = []
    orient = randint(1,2)

    num = randint(1,10)
    letternum = randint(1,10)
    try: 
        if int(orient) == 1:
            for i in range(2):
                if newComputerBoard[num][letternum+i] == "-":
                    newComputerBoard[num][letternum+i] = "X"
                    PatrolBoat.append(letters[letternum+i]+str(num))
                else:
                    return 0

        elif int(orient) == 2:
            for i in range(2):
                if newComputerBoard[num-i][letternum] == "-":
                    newComputerBoard[num-i][letternum] = "X"
                    PatrolBoat.append(letters[letternum]+str(num-i))
                else:
                    return 0
        else: 
            return 0
    
    except IndexError:
        return 0
    
    except ValueError:
        return 0
    
    newComputerShips["PatrolBoat"] = PatrolBoat
    return [newComputerBoard,newComputerShips]

def computerInit(computerBoard,computerShips):
    global dev
    params = cCarrier(computerBoard,computerShips)
    while params == 0:
        params = cCarrier(computerBoard,computerShips)
    computerBoard = params[0]
    computerShips = params[1]

    if dev == 1:
        print()
        for i in computerBoard:
                for j in i: 
                    print(j,end=" ")
                print()
        print()
    
    params = cBattleship(computerBoard,computerShips)
    while params == 0:
        params = cBattleship(computerBoard,computerShips)
    computerBoard = params[0]
    computerShips = params[1]
    
    if dev == 1:
        print()
        for i in computerBoard:
                for j in i: 
                    print(j,end=" ")
                print()
        print()

    params = cDestroyer(computerBoard,computerShips)
    while params == 0:
        params = cDestroyer(computerBoard,computerShips)
    computerBoard = params[0]
    computerShips = params[1]
    
    if dev == 1:
        print()
        for i in computerBoard:
                for j in i: 
                    print(j,end=" ")
                print()
        print()
    
    params = cSubmarine(computerBoard,computerShips)
    while params == 0:
        params = cSubmarine(computerBoard,computerShips)
    computerBoard = params[0]
    computerShips = params[1]
    
    if dev == 1:
        print()
        for i in computerBoard:
                for j in i: 
                    print(j,end=" ")
                print()
        print()
    
    params = cPatrolBoat(computerBoard,computerShips)
    while params == 0:
        params = cPatrolBoat(computerBoard,computerShips)
    computerBoard = params[0]
    computerShips = params[1]

    if dev == 1:
        print()
        for i in computerBoard:
                for j in i: 
                    print(j,end=" ")
                print()
        print()

    return [computerBoard,computerShips]

'''
COMPUTER TURN
'''

def coordPicker(computerAttempts):
    global lastHit
    if lastHit == 0:
        num = randint(1,10)
        letternum = randint(1,10)
        letter = letters[letternum]
        coord = letter+str(num)
        return [num,letternum,coord]
    else:
        letter = lastHit[0]
        num = int(lastHit[1:])
        letternum = int(letters.index(letter))
        while True:
            location = randint(1,4)
            if location == 1:
                coord = letters[letternum+1]+str(num)
                if computerAttempts[num][letternum+1] == "-":
                    return [num, letternum+1, coord]
            elif location == 2:
                coord = letters[letternum]+str(num-1)
                if computerAttempts[num-1][letternum] == "-":
                    return [num-1, letternum, coord]
            elif location == 3:
                coord = letters[letternum-1]+str(num)
                if computerAttempts[num][letternum-1] == "-":
                    return [num, letternum+1, coord]
            else:
                coord = letters[letternum]+str(num-1)
                if computerAttempts[num-1][letternum] == "-":
                    return [num-1, letternum, coord]
              
def computerTurn(computerAttempts,playerShips,defender):
    global lastHit
    params = coordPicker(computerAttempts)
    num = params[0]
    letternum = params[1]
    coord = params[2]

    if coord in playerShips["Carrier"]:
        computerAttempts[num][letternum] = "H"
        print(f"{coord} WAS A HIT!")
        playerShips["Carrier"].remove(coord)
        lastHit = coord
        if len(playerShips["Carrier"]) == 0:
            print("Carrier has sunk! ")
            lastHit = 0

    elif coord in playerShips["Battleship"]:
        computerAttempts[num][letternum] = "H"
        print(f"{coord} WAS A HIT!")
        playerShips["Battleship"].remove(coord)
        lastHit = coord
        if len(playerShips["Battleship"]) == 0:
            print("Battleship has sunk! ")
            lastHit = 0

    elif coord in playerShips["Destroyer"]:
        computerAttempts[num][letternum] = "H"
        print(f"{coord} WAS A HIT!")
        playerShips["Destroyer"].remove(coord)
        lastHit = coord
        if len(playerShips["Destroyer"]) == 0:
            print("Destroyer has sunk! ")
            lastHit = 0

    elif coord in playerShips["Submarine"]:
        computerAttempts[num][letternum] = "H"
        print(f"{coord} WAS A HIT!")
        playerShips["Submarine"].remove(coord)
        lastHit = coord
        if len(playerShips["Submarine"]) == 0:
            print("Submarine has sunk! ")
            lastHit = 0

    elif coord in playerShips["PatrolBoat"]:
        computerAttempts[num][letternum] = "H"
        print(f"{coord} WAS A HIT!")
        playerShips["PatrolBoat"].remove(coord)
        lastHit = coord 
        if len(playerShips["PatrolBoat"]) == 0:
            print("Patrol Boat has sunk! ")
            lastHit = 0

    else:
        if computerAttempts[num][letternum] == "H" or computerAttempts[num][letternum] == "M":
            computerTurn(computerAttempts,playerShips,defender)
        else:
            computerAttempts[num][letternum] = "M"
            print(f"{coord} WAS A MISS!")

'''
RUNNING PROGRAM
'''

def rules():
    print("RULES OF THE GAME:\n")
    print("1. The game is played on a 10x10 grid. Here is the virtual grid: ")
    print("""
        XX A B C D E F G H I J
        01 - - - - - - - - - - 
        02 - - - - - - - - - - 
        03 - - - - - - - - - -
        04 - - - - - - - - - - 
        05 - - - - - - - - - - 
        06 - - - - - - - - - -
        07 - - - - - - - - - -
        08 - - - - - - - - - - 
        09 - - - - - - - - - - 
        10 - - - - - - - - - -  
          """)
    print("2. Each player has 5 ships of different sizes:")
    print("   - Carrier (5 spaces)")
    print("   - Battleship (4 spaces)")
    print("   - Destroyer (3 spaces)")
    print("   - Submarines (3 spaces)")
    print("   - Patrol Boat (2 spaces)")
    print("3. Ships can be placed horizontally or vertically but cannot overlap.")
    print("4. Players take turns guessing coordinates (following format: 'B4') to attack.")
    print("5. If a ship occupies the guessed location, it's a 'HIT'; otherwise, it's a 'MISS'.")
    print("6. When all parts of a ship are hit, it is 'SUNK'.")
    print("7. The first player to sink all of their opponent’s ships wins!")
    print("\nGet ready to battle! Press any key to continue! 🚢💥")
    input()

def main():

    '''
    VARIABLES
    '''

    global dev
    player1Board = [
            ["XX","A","B","C","D","E","F","G","H","I","J"],
            ["01","-","-","-","-","-","-","-","-","-","-"],
            ["02","-","-","-","-","-","-","-","-","-","-"],
            ["03","-","-","-","-","-","-","-","-","-","-"],
            ["04","-","-","-","-","-","-","-","-","-","-"],
            ["05","-","-","-","-","-","-","-","-","-","-"],
            ["06","-","-","-","-","-","-","-","-","-","-"],
            ["07","-","-","-","-","-","-","-","-","-","-"],
            ["08","-","-","-","-","-","-","-","-","-","-"],
            ["09","-","-","-","-","-","-","-","-","-","-"],
            ["10","-","-","-","-","-","-","-","-","-","-"]
        ]
    player2Board = [
            ["XX","A","B","C","D","E","F","G","H","I","J"],
            ["01","-","-","-","-","-","-","-","-","-","-"],
            ["02","-","-","-","-","-","-","-","-","-","-"],
            ["03","-","-","-","-","-","-","-","-","-","-"],
            ["04","-","-","-","-","-","-","-","-","-","-"],
            ["05","-","-","-","-","-","-","-","-","-","-"],
            ["06","-","-","-","-","-","-","-","-","-","-"],
            ["07","-","-","-","-","-","-","-","-","-","-"],
            ["08","-","-","-","-","-","-","-","-","-","-"],
            ["09","-","-","-","-","-","-","-","-","-","-"],
            ["10","-","-","-","-","-","-","-","-","-","-"]
        ]
    playerBoard = [
            ["XX","A","B","C","D","E","F","G","H","I","J"],
            ["01","-","-","-","-","-","-","-","-","-","-"],
            ["02","-","-","-","-","-","-","-","-","-","-"],
            ["03","-","-","-","-","-","-","-","-","-","-"],
            ["04","-","-","-","-","-","-","-","-","-","-"],
            ["05","-","-","-","-","-","-","-","-","-","-"],
            ["06","-","-","-","-","-","-","-","-","-","-"],
            ["07","-","-","-","-","-","-","-","-","-","-"],
            ["08","-","-","-","-","-","-","-","-","-","-"],
            ["09","-","-","-","-","-","-","-","-","-","-"],
            ["10","-","-","-","-","-","-","-","-","-","-"]
        ]
    computerBoard = [
            ["XX","A","B","C","D","E","F","G","H","I","J"],
            ["01","-","-","-","-","-","-","-","-","-","-"],
            ["02","-","-","-","-","-","-","-","-","-","-"],
            ["03","-","-","-","-","-","-","-","-","-","-"],
            ["04","-","-","-","-","-","-","-","-","-","-"],
            ["05","-","-","-","-","-","-","-","-","-","-"],
            ["06","-","-","-","-","-","-","-","-","-","-"],
            ["07","-","-","-","-","-","-","-","-","-","-"],
            ["08","-","-","-","-","-","-","-","-","-","-"],
            ["09","-","-","-","-","-","-","-","-","-","-"],
            ["10","-","-","-","-","-","-","-","-","-","-"]
        ]
    player1Ships = {}
    player2Ships = {}
    playerShips = {}
    computerShips = {}
    player1Attempts = [
            ["XX","A","B","C","D","E","F","G","H","I","J"],
            ["01","-","-","-","-","-","-","-","-","-","-"],
            ["02","-","-","-","-","-","-","-","-","-","-"],
            ["03","-","-","-","-","-","-","-","-","-","-"],
            ["04","-","-","-","-","-","-","-","-","-","-"],
            ["05","-","-","-","-","-","-","-","-","-","-"],
            ["06","-","-","-","-","-","-","-","-","-","-"],
            ["07","-","-","-","-","-","-","-","-","-","-"],
            ["08","-","-","-","-","-","-","-","-","-","-"],
            ["09","-","-","-","-","-","-","-","-","-","-"],
            ["10","-","-","-","-","-","-","-","-","-","-"]
        ]
    player2Attempts = [
            ["XX","A","B","C","D","E","F","G","H","I","J"],
            ["01","-","-","-","-","-","-","-","-","-","-"],
            ["02","-","-","-","-","-","-","-","-","-","-"],
            ["03","-","-","-","-","-","-","-","-","-","-"],
            ["04","-","-","-","-","-","-","-","-","-","-"],
            ["05","-","-","-","-","-","-","-","-","-","-"],
            ["06","-","-","-","-","-","-","-","-","-","-"],
            ["07","-","-","-","-","-","-","-","-","-","-"],
            ["08","-","-","-","-","-","-","-","-","-","-"],
            ["09","-","-","-","-","-","-","-","-","-","-"],
            ["10","-","-","-","-","-","-","-","-","-","-"]
        ]
    playerAttempts = [
            ["XX","A","B","C","D","E","F","G","H","I","J"],
            ["01","-","-","-","-","-","-","-","-","-","-"],
            ["02","-","-","-","-","-","-","-","-","-","-"],
            ["03","-","-","-","-","-","-","-","-","-","-"],
            ["04","-","-","-","-","-","-","-","-","-","-"],
            ["05","-","-","-","-","-","-","-","-","-","-"],
            ["06","-","-","-","-","-","-","-","-","-","-"],
            ["07","-","-","-","-","-","-","-","-","-","-"],
            ["08","-","-","-","-","-","-","-","-","-","-"],
            ["09","-","-","-","-","-","-","-","-","-","-"],
            ["10","-","-","-","-","-","-","-","-","-","-"]
        ]
    computerAttempts = [
            ["XX","A","B","C","D","E","F","G","H","I","J"],
            ["01","-","-","-","-","-","-","-","-","-","-"],
            ["02","-","-","-","-","-","-","-","-","-","-"],
            ["03","-","-","-","-","-","-","-","-","-","-"],
            ["04","-","-","-","-","-","-","-","-","-","-"],
            ["05","-","-","-","-","-","-","-","-","-","-"],
            ["06","-","-","-","-","-","-","-","-","-","-"],
            ["07","-","-","-","-","-","-","-","-","-","-"],
            ["08","-","-","-","-","-","-","-","-","-","-"],
            ["09","-","-","-","-","-","-","-","-","-","-"],
            ["10","-","-","-","-","-","-","-","-","-","-"]
        ]
    
    '''
    MENU
    '''
    
    print("\n\t********************************\n\tWELCOME TO BATTLESHIP SIMULATOR\n\t********************************\n")
    print("Select Mode: ")
    print("1. Developer mode")
    print("2. Player mode")

    try:
        dev = int(input("Enter (1-2): "))
        if dev == 1 or dev == 2:
            pass
        else:
            dev = 2
            print("Defaulting to player mode")
    except:
        print("Invalid number choice! Restaring program....")
        return

    print("\nSelect Game Style: ")
    print("1. Rules")
    print("2. Start PlayerVsPlayer")
    print("3. Start Single Player Mode")
    print("4. Quit")

    try:
        mode = int(input("Enter (1-4): "))
        if mode == 1:
            rules()
        elif mode == 2:
            print("Starting Battleship Simulator.....\n")
            time.sleep(2)
            print("Beginning Player 1 setup...")
            time.sleep(2)
            params1 = playerInit(player1Board, player1Ships)
            player1Board = params1[0]
            player1Ships = params1[1]
            if player1Board == 0:
                return
            print("We now clear screen to cover the setup:")
            time.sleep(2)
            os.system("cls" if os.name == "nt" else "clear")

            print("Beginning Player 2 setup...")
            time.sleep(2)
            params2 = playerInit(player2Board, player2Ships)
            player2Board = params2[0]
            player2Ships = params2[1]
            if player2Board == 0:
                return
            print("We now clear screen to cover the setup:")
            time.sleep(2)
            os.system("cls" if os.name == "nt" else "clear")
            print("Setup finished! Loading game...")
            time.sleep(2)

            pointer = 1
            while True:
                if pointer%2 == 1:
                    while True: 
                        print("Player 1")
                        print("Choose what to do: ")
                        print("1. Show past attempts")
                        print("2. Show my placements")
                        print("3. Make a guess and end turn")
                        print("4. End game")
                        try:
                            choice = int(input("Enter number (1-4): "))
                            if choice > 4 or choice < 1:
                                print('Invalid choice! Try again! ')
                                continue
                        except:
                            print('Invalid choice! Try again! ')
                            continue
                        if choice == 1: 
                            print("The previous attempts: ")
                            for i in player1Attempts:
                                for j in i: 
                                    print(j,end=" ")
                                print()
                            print()
                        elif choice == 2: 
                            print("The placement grid is as follows: ")
                            for i in player1Board:
                                for j in i: 
                                    print(j,end=" ")
                                print()
                            print()
                        elif choice == 3:
                            out = playerTurn(player1Attempts,player2Ships)
                            while out == 1:
                                print()
                                out = playerTurn(player1Attempts,player2Ships)

                            if len(player2Ships["Carrier"]) == 0 and len(player2Ships["Battleship"]) == 0 and len(player2Ships["Destroyer"]) == 0 and len(player2Ships["Submarine"]) == 0 and len(player2Ships["PatrolBoat"]) == 0:
                                print(f"All the boats of Player 2 have sunk!")
                                print("Player 1 is the WINNER!!!")
                                return

                            time.sleep(2)
                            print("We now insert clear screen to cover the turn:")
                            time.sleep(2)
                            os.system("cls" if os.name == "nt" else "clear")
                            break
                        elif choice == 4:
                            print("Player 2 is the WINNER by resignation")
                            return
                        else:
                            print("Error! Try again ")

                else:
                    while True: 
                        print("Player 2")
                        print("Choose what to do: ")
                        print("1. Show past attempts")
                        print("2. Show my placements")
                        print("3. Make a guess and end turn")
                        print("4. End game")
                        try:
                            choice = int(input("Enter number (1-4): "))
                            if choice > 4 or choice < 1:
                                print('Invalid choice! Try again! ')
                                continue
                        except:
                            print('Invalid choice! Try again! ')
                            continue
                        if choice == 1: 
                            print("The previous attempts: ")
                            for i in player2Attempts:
                                for j in i: 
                                    print(j,end=" ")
                                print()
                            print()
                        elif choice == 2: 
                            print("The placement grid is as follows: ")
                            for i in player2Board:
                                for j in i: 
                                    print(j,end=" ")
                                print()
                            print()
                        elif choice == 3:
                            out = playerTurn(player2Attempts,player1Ships)
                            while out == 1:
                                print()
                                out = playerTurn(player2Attempts,player1Ships)
                            if len(player1Ships["Carrier"]) == 0 and len(player1Ships["Battleship"]) == 0 and len(player1Ships["Destroyer"]) == 0 and len(player1Ships["Submarine"]) == 0 and len(player1Ships["PatrolBoat"]) == 0:
                                print(f"All the boats of Player 1 have sunk!")
                                print("Player 2 is the WINNER!!!")
                                return

                            time.sleep(2)
                            print("We now clear screen to cover the turn:")
                            time.sleep(2)
                            os.system("cls" if os.name == "nt" else "clear")
                            break

                        elif choice == 4:
                            print("Player 1 is the WINNER by resignation")
                            return
                        else:
                            print("Error! Try again ")
                pointer += 1
        elif mode == 3:
            print("Starting Battleship Simulator.....\n")
            time.sleep(2)
            print("Beginning Player setup...")
            time.sleep(2)
            params1 = playerInit(playerBoard, playerShips)
            playerBoard = params1[0]
            playerShips = params1[1]
            if playerBoard == 0:
                return
            print("We now clear screen to cover the setup:")
            time.sleep(2)
            os.system("cls" if os.name == "nt" else "clear")

            print("Beginning Computer setup...")
            time.sleep(2)
            params2 = computerInit(computerBoard,computerShips)
            computerBoard = params2[0]
            computerShips = params2[1]
            cont = input("Press any key to continue! ")
            print("Setup finished! Loading game...")
            time.sleep(2)

            pointer = 1
            while True:
                if pointer%2 == 1:
                    while True: 
                        print("Player")
                        print("Choose what to do: ")
                        print("1. Show past attempts")
                        print("2. Show my placements")
                        print("3. Make a guess and end turn")
                        print("4. End game")
                        try:
                            choice = int(input("Enter number (1-4): "))
                            if choice > 4 or choice < 1:
                                print('Invalid choice! Try again! ')
                                print()
                                continue
                        except:
                            print('Invalid choice! Try again! ')
                            print()
                            continue
                        if choice == 1: 
                            print("The previous attempts: ")
                            for i in playerAttempts:
                                for j in i: 
                                    print(j,end=" ")
                                print()
                            print()
                        elif choice == 2: 
                            print("The placement grid is as follows: ")
                            for i in playerBoard:
                                for j in i: 
                                    print(j,end=" ")
                                print()
                            print()
                        elif choice == 3:
                            out = playerTurn(playerAttempts,computerShips)
                            while out == 1:
                                print()
                                out = playerTurn(playerAttempts,computerShips)
                            if len(computerShips["Carrier"]) == 0 and len(computerShips["Battleship"]) == 0 and len(computerShips["Destroyer"]) == 0 and len(computerShips["Submarine"]) == 0 and len(computerShips["PatrolBoat"]) == 0:
                                print(f"All the boats of Computer have sunk!")
                                print("Player is the WINNER!!!")
                                return
                            
                            time.sleep(2)
                            print("We now insert clear screen to cover the turn:")
                            time.sleep(2)
                            os.system("cls" if os.name == "nt" else "clear")
                            break
                        elif choice == 4:
                            print("Computer is the WINNER by resignation")
                            return
                        else:
                            print("Error! Try again ")
                else:
                    while True: 
                        print("Computer")
                        computerTurn(computerAttempts,playerShips)
                        if len(playerShips["Carrier"]) == 0 and len(playerShips["Battleship"]) == 0 and len(playerShips["Destroyer"]) == 0 and len(playerShips["Submarine"]) == 0 and len(playerShips["PatrolBoat"]) == 0:
                                print(f"All the boats of Player have sunk!")
                                print("Computer is the WINNER!!!")
                                return
                        cont = input("Press any key to continue: ")
                        print("We now clear screen to cover the turn:")
                        time.sleep(2)
                        os.system("cls" if os.name == "nt" else "clear")
                        break
                pointer += 1
        elif mode == 4:
            return 404
        else:
            print("Invalid number choice! Restaring program....")
            return    
    except:
        print("Invalid number choice! Restaring program....")
        return

if __name__ == "__main__":
    while True: 
        code = main()
        if code == 404:
            break
