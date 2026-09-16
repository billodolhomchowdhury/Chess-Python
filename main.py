# print("R|K|B|Q|H|B|K|R")
TempSqNameHolder = ""
SelectedBlock = ""
SavedWhiteKingPos = ""
SavedBlackKingPos = ""
SelectedPawn = ""
Ab = {"1": "A", "2":"B", "3":"C", "4":"D", "5":"E", "6":"F", "7":"G", "8":"H"}
Ab2 = {}
Data={  "AA":"R","AB":"K","AC":"B","AD":"Q","AE":"H","AF":"B","AG":"K","AH":"R",
        "BA":"P","BB":"P","BC":"P","BD":"P","BE":"P","BF":"P","BG":"P","BH":"P",
        "CA":" ","CB":" ","CC":" ","CD":" ","CE":" ","CF":" ","CG":" ","CH":" ",
        "DA":" ","DB":" ","DC":" ","DD":" ","DE":" ","DF":" ","DG":" ","DH":" ",
        "EA":" ","EB":" ","EC":" ","ED":" ","EE":" ","EF":" ","EG":" ","EH":" ",
        "FA":" ","FB":" ","FC":" ","FD":" ","FE":" ","FF":" ","FG":" ","FH":" ",
        "GA":"P","GB":"P","GC":"P","GD":"P","GE":"P","GF":"P","GG":"P","GH":"P",
        "HA":"R","HB":"K","HC":"B","HD":"Q","HE":"H","HF":"B","HG":"K","HH":"R",
      }


def Update():
    print("| 1 || 2 || 3 || 4 || 5 || 6 || 7 || 8 |")
    for r in range(8,0,-1):
        row = r
        for column in range(1,9):
            TempSqNameHolder = ""
            TempSqNameHolder = TempSqNameHolder+Ab[str(row)]+Ab[str(column)]
            # print(TempSqNameHolder)
            print("|",Data[str(TempSqNameHolder)],"|", end="")
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
    ISTNC_Out = Ab[ISTNC_Process_F]+Ab[ISTNC_Process_B]
    print(ISTNC_Out)
    

def AskForInput():
    SelectedBlock = int(input("Select A Fighter: "))
    print(InputNumberToStringConverter(SelectedBlock))
    AttackingBlock = int(input("Select A Sq to Move: "))
    print(InputNumberToStringConverter(AttackingBlock))
    return SelectedBlock,AttackingBlock

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
    Data[SelectedPawnLocationString]=" "
    Data[AttackingPawnLocationString]=SelectedPawn

def CheckPawnMoveValidity():
    pass

def CheckKingsSafety():
    pass

GameRunning = True
# while GameRunning !=False:
#     SelectedBlock, AttackingBlock = AskForInput()
#     UpdatePos(SelectedBlock, AttackingBlock)
#     Update()
#     print(SavedWhiteKingPos)
InputStringToNumberConverter("AA")