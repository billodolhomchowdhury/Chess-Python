# print("R|K|B|Q|H|B|K|R")
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
BOLD = "\033[1m"
RESET = "\033[0m"
TempSqNameHolder = ""
SelectedBlock = ""
SavedWhiteKingPos = ""
SavedBlackKingPos = ""
SelectedPawn = ""
Ab = {"1": "A", "2":"B", "3":"C", "4":"D", "5":"E", "6":"F", "7":"G", "8":"H"}
Ab2 = {"A": "1", "B": "2","C":"3","D":"4","E":"5","F":"6","G":"7","H":"8"}
Data={  "AA":"WR","AB":"WK","AC":"WB","AD":"WQ","AE":"WH","AF":"WB","AG":"WK","AH":"WR",
        "BA":"WP","BB":"WP","BC":"WP","BD":"WP","BE":"WP","BF":"WP","BG":"WP","BH":"WP",
        "CA":"   ","CB":"   ","CC":"   ","CD":"   ","CE":"   ","CF":"   ","CG":"   ","CH":"   ",
        "DA":"   ","DB":"   ","DC":"   ","DD":"   ","DE":"   ","DF":"   ","DG":"   ","DH":"   ",
        "EA":"   ","EB":"   ","EC":"   ","ED":"   ","EE":"   ","EF":"   ","EG":"   ","EH":"   ",
        "FA":"   ","FB":"   ","FC":"   ","FD":"   ","FE":"   ","FF":"   ","FG":"   ","FH":"   ",
        "GA":"SP","GB":"SP","GC":"SP","GD":"SP","GE":"SP","GF":"SP","GG":"SP","GH":"SP",
        "HA":"SR","HB":"SK","HC":"SB","HD":"SQ","HE":"SH","HF":"SB","HG":"SK","HH":"SR",
      }

Icons = {   "WH":" ♚ ", "WQ":" ♛ ", "WR":" ♜ ","WB":" ♝ ","WK":" ♞ ","WP":" ♟ ",
            "SH":" ♔ ", "SQ":" ♕ ", "SR":" ♖ ","SB":" ♗ ","SK":" ♘ ","SP":" ♙ ",
            "   ": "   "
        }


def color_text(text, color_code):
    return f"{color_code}{text}\033[0m"

def Update():
    print(f"{color_text("|   ||   1  ||  2   ||   3  ||   4  ||   5  ||   6  ||   7  ||   8  |",RED)}")
    for r in range(8,0,-1):
        row = r
        print(color_text(f"| {r} |",RED),end="")
        for column in range(1,9):
            TempSqNameHolder = ""
            TempSqNameHolder = TempSqNameHolder+Ab[str(row)]+Ab[str(column)]
            print("|",Icons[Data[str(TempSqNameHolder)]]," |", end="")
        print("")

def InputNumberToStringConverter(INTSC_DATA_INPUT):
    BlockRow = str(INTSC_DATA_INPUT//10)
    BlockRow = Ab[BlockRow]
    BlockColumn = str(INTSC_DATA_INPUT%10)
    BlockColumn = Ab[BlockColumn]
    return BlockRow+BlockColumn

def InputStringToNumberConverter(ISTNC_DATA_INPUT):
    ISTNC_Process_F = ISTNC_DATA_INPUT[0]
    ISTNC_Process_B = ISTNC_DATA_INPUT[1]
    ISTNC_Out = Ab2[ISTNC_Process_F]+Ab2[ISTNC_Process_B]
#     print(ISTNC_Out)
# def InputNumberToStringConverter(INTSC_DATA_INPUT):
#     BlockRow = INTSC_DATA_INPUT//100
#     BlockColumn = INTSC_DATA_INPUT%100
#     BlockRow = chr(BlockRow+64)
#     BlockColumn = chr(BlockColumn+64)
#     print(BlockRow+BlockColumn)

    

def AskForInput():
    SelectedBlock = int(input("Select A Fighter: "))
    print(InputNumberToStringConverter(SelectedBlock))
    AttackingBlock = int(input("Select A Sq to Move: "))
    print(InputNumberToStringConverter(AttackingBlock))
    return SelectedBlock+64,AttackingBlock+64

def UpdatePos(UpdatePosSelectedPawnData, UpdatePosAttackingPawnData):
    global SavedWhiteKingPos
    global SelectedPawn
    global SelectedPawnLocationString
    global AttackingPawnLocationString
    SelectedPawnLocationString = str(InputNumberToStringConverter(UpdatePosSelectedPawnData))
    AttackingPawnLocationString = str(InputNumberToStringConverter(UpdatePosAttackingPawnData))
    SelectedPawn = Data[SelectedPawnLocationString]
    AttackingPawn = Data[AttackingPawnLocationString]
    if(SelectedPawn=="H"):
        SavedWhiteKingPos = AttackingPawnLocationString
    Data[SelectedPawnLocationString]="   "
    Data[AttackingPawnLocationString]=SelectedPawn

def CheckPawnMoveValidity():
    pass

# def HorizontalCheck(Position):
#     Position = InputStringToNumberConverter(Position)
#     PosY = Position%10
#     PosX = Position//10
#     for i in range(1,9):
#         if Data[]
#     pass

def CheckKingsSafety():
    pass

GameRunning = True
while GameRunning !=False:
    SelectedBlock, AttackingBlock = AskForInput()
    UpdatePos(SelectedBlock, AttackingBlock)
    Update()
    print(SavedWhiteKingPos)
# InputStringToNumberConverter("AA")
# InputNumberToStringConverter(int(input("Enter a Number: ")))
