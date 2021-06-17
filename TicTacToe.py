import os

isActive = True

boxes = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

table = f"\n    {boxes[0]} | {boxes[1]} | {boxes[2]}\n    --+---+---\n    {boxes[3]} | {boxes[4]} | {boxes[5]}\n    --+---+---\n    {boxes[6]} | {boxes[7]} | {boxes[8]}\n"

def check4victory(boxes):
    #X:
    if boxes[0] == 'X' and boxes[1] == 'X' and boxes[2] == 'X' or boxes[3] == 'X' and boxes[4] == 'X' and boxes[5] == 'X' or boxes[6] == 'X' and boxes[7] == 'X' and boxes[8] == 'X' or boxes[0] == 'X' and boxes[3] == 'X' and boxes[6] == 'X' or boxes[1] == 'X' and boxes[4] == 'X' and boxes[7] == 'X' or boxes[2] == 'X' and boxes[5] == 'X' and boxes[8] == 'X' or boxes[0] == 'X' and boxes[4] == 'X' and boxes[8] == 'X' or boxes[2] == 'X' and boxes[4] == 'X' and boxes[6] == 'X':
        print('Player X Wins!')
        return 0
    #O:
    if boxes[0] == 'O' and boxes[1] == 'O' and boxes[2] == 'O' or boxes[3] == 'O' and boxes[4] == 'O' and boxes[5] == 'O' or boxes[6] == 'O' and boxes[7] == 'O' and boxes[8] == 'O' or boxes[0] == 'O' and boxes[3] == 'O' and boxes[6] == 'O' or boxes[1] == 'O' and boxes[4] == 'O' and boxes[7] == 'O' or boxes[2] == 'O' and boxes[5] == 'O' and boxes[8] == 'O' or boxes[0] == 'O' and boxes[4] == 'O' and boxes[8] == 'O' or boxes[2] == 'O' and boxes[4] == 'O' and boxes[6] == 'O':
        print("Player O Wins!")
        return 0
        
os.system("clear")
print(table)

while isActive:
    
    while 1:
            move = int(input("What box choose player X? ")) - 1
            if move in range(0,9):
                if boxes[move] == " ":
                    boxes[move] = 'X'
                    break
                else: print("Bad Placement")

            else: print("Bad Placement")
                
    table = f"\n    {boxes[0]} | {boxes[1]} | {boxes[2]}\n    --+---+---\n    {boxes[3]} | {boxes[4]} | {boxes[5]}\n    --+---+---\n    {boxes[6]} | {boxes[7]} | {boxes[8]}\n"

    os.system("clear")
    print(table)
    if check4victory(boxes) == 0:
            break
            
    while 1:
            move = int(input("What box choose player O? ")) - 1
            if move in range(0,9):
                if boxes[move] == " ":
                    boxes[move] = 'O'
                    break
                else: print("Bad Placement")
                
            else: print("Bad Placement")
                
        
    table = f"\n    {boxes[0]} | {boxes[1]} | {boxes[2]}\n    --+---+---\n    {boxes[3]} | {boxes[4]} | {boxes[5]}\n    --+---+---\n    {boxes[6]} | {boxes[7]} | {boxes[8]}\n"

    os.system("clear")
    print(table)
    if check4victory(boxes) == 0:
        break
