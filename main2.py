# print("R|K|B|Q|H|B|K|R")
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
BOLD = "\033[1m"
RESET = "\033[0m"
GameRunning = True
CurrentlyCheckMated = False
TempSqNameHolder = ""
SelectedBlock = ""
SavedWhiteKingPos = "AE"  #CHANGE LATER BE CAREFULL BILL
SavedBlackKingPos = "HE"
SelectedPawn = ""
PreviouslyData = {}
CheckmatedDuration = 0
PreviousSelectedBlock =""
PreviousSelectedBlockPawn = ""
PreviousAttackingBlock = ""
PreviousAttackingBlockPawn = ""
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

PawnsAbilityData = {
    "PREFIX": "StraightPos?| DiagonalPos?|",
    "H":"YY", "Q":"YY", "B":"NY", "R":"YN","P":"YN"
}

PawnsRangeData = {
    "H":"11111", 
    "Q":"88888",
    "R":"88880", 
    "P":"10000", 
    "B":"00008"
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
    ISTNC_Out = int(Ab2[ISTNC_Process_F]+Ab2[ISTNC_Process_B])
    return ISTNC_Out

# def InputNumberToStringConverter(INTSC_DATA_INPUT):
#     BlockRow = INTSC_DATA_INPUT//100
#     BlockColumn = INTSC_DATA_INPUT%100
#     BlockRow = chr(BlockRow+64)
#     BlockColumn = chr(BlockColumn+64)
#     print(BlockRow+BlockColumn)

    

def AskForInput():
    SelectedBlock = int(input("Select A Fighter: "))
    # print(InputNumberToStringConverter(SelectedBlock))
    AttackingBlock = int(input("Select A Sq to Move: "))
    # print(InputNumberToStringConverter(AttackingBlock))
    return SelectedBlock,AttackingBlock # NOte TO MYSELF: ADD 64 FOR ASCII Value

def UpdatePos(UpdatePosSelectedPawnData, UpdatePosAttackingPawnData):
    global SavedWhiteKingPos
    global SelectedPawn
    global SelectedPawnLocationString
    global AttackingPawnLocationString
    global PreviousSelectedBlock
    global PreviousSelectedBlockPawn
    global PreviousAttackingBlock
    global PreviousAttackingBlockPawn
    global AttackingPawn
    SelectedPawnLocationString = str(InputNumberToStringConverter(UpdatePosSelectedPawnData))
    PreviousSelectedBlock = SelectedPawnLocationString
    # print("SELEECTED PAWN STRING LOCATION: ",SelectedPawnLocationString)
    AttackingPawnLocationString = str(InputNumberToStringConverter(UpdatePosAttackingPawnData))
    SelectedPawn = Data[SelectedPawnLocationString]
    AttackingPawn = Data[AttackingPawnLocationString]
    if(SelectedPawn=="WH"):
        SavedWhiteKingPos = AttackingPawnLocationString
    Data[SelectedPawnLocationString]="   "
    Data[AttackingPawnLocationString]=SelectedPawn

def RevertChanges():
    Data[SelectedPawnLocationString] = SelectedPawn
    Data[AttackingPawnLocationString] = AttackingPawn

def CheckPawnMoveValidity():
    pass

def HorizontalCheck(Position):
    LeftStatusIsSafe = True
    LeftUnsafePawn = ""
    RightStatusIsSafe = True
    RightUnsafePawn = ""
    LeftDanPawnLocation = 0
    RightDanPawnLocation = 0
    Himself = Data[Position]
    Position = InputStringToNumberConverter(Position)
    HimselfTeam = Himself[0]
    PosY = Position//10 
    PosX = Position%10
    PosYASCIIINT = PosY+64
    PosXASCIIINT = PosX+64
    # LEFT CHECK ---------------- X --------- X ----
    for i in range(1,PosX):
        Temp_HC_Left_Value_Data = Data[chr(PosYASCIIINT)+chr(PosXASCIIINT-i)]
        if(Temp_HC_Left_Value_Data[0]==HimselfTeam):
            # print("LEFT : ===== K")
            # LeftStatusIsSafe =  "HI of FRI"
            pass
        elif Temp_HC_Left_Value_Data[0]==" ":
            # print("LEFT : ===== Empty")
            pass
        else:
            # print("LEFT : ===== Dangerous")
            # LeftStatusIsSafe =  "HI of Dan"
            LeftStatusIsSafe = False
            LeftUnsafePawn = Temp_HC_Left_Value_Data
            LeftDanPawnLocation = i
            break
            

# RIGHT CHECK ---------------- X --------- X ----

    for i in range(PosX+1,9):
        Temp_HC_Right_Value_Data = Data[chr(PosYASCIIINT)+chr(PosXASCIIINT+i-PosX)]
        if(Temp_HC_Right_Value_Data[0]==HimselfTeam):
            # print("RIGHT : ===== K")
            # RightStatusIsSafe =  "HI of FRI"
            pass
        elif Temp_HC_Right_Value_Data[0]==" ":
            # print("RIGHT : ===== Empty")
            pass
        else:
            # print("RIGHT : ===== Dangerous")
            # RightStatusIsSafe =  "HI of Dan"
            RightStatusIsSafe = False
            RightUnsafePawn = Temp_HC_Right_Value_Data
            RightDanPawnLocation = i - PosX+1
            break

    return LeftStatusIsSafe,RightStatusIsSafe,LeftUnsafePawn,RightUnsafePawn,LeftDanPawnLocation,RightDanPawnLocation


def VerticalCheck(Position):
    UpStatusIsSafe = True
    UpUnsafePawn = ""
    DownStatusIsSafe = True
    DownUnsafePawn = ""
    UpDanPawnLocation = 0
    DownDanPawnLocation = 0
    Himself = Data[Position]
    Position = InputStringToNumberConverter(Position)
    HimselfTeam = Himself[0]
    PosY = Position//10 
    PosX = Position%10
    PosYASCIIINT = PosY+64
    PosXASCIIINT = PosX+64
    # Up CHECK ---------------- X --------- X ----
    for i in range(1,9-PosY):
        Temp_HC_Up_Value_Data = Data[chr(PosYASCIIINT+i)+chr(PosXASCIIINT)]
        if(Temp_HC_Up_Value_Data[0]==HimselfTeam):
            # print("UP : ===== K")
        #     # LeftStatusIsSafe =  "HI of FRI"
            pass
        elif Temp_HC_Up_Value_Data[0]==" ":
            # print("UP : ===== Empty")
            pass
        else:
            # print("UP : ===== Dangerous")
        #     # LeftStatusIsSafe =  "HI of Dan"
            UpStatusIsSafe = False
            UpUnsafePawn = Temp_HC_Up_Value_Data
            UpDanPawnLocation = i
            break
        # print(i)
            

# Down CHECK ---------------- X --------- X ----

    for i in range(PosY-1,0,-1):
        Temp_HC_Down_Value_Data = Data[chr(PosYASCIIINT+i-PosY)+chr(PosXASCIIINT)]
        if(Temp_HC_Down_Value_Data[0]==HimselfTeam):
            # print("Down : ===== K")
    #         # RightStatusIsSafe =  "HI of FRI"
            pass
        elif Temp_HC_Down_Value_Data[0]==" ":
            # print("Down : ===== Empty")
            pass
        else:
            # print("Down : ===== Dangerous")
    #         # RightStatusIsSafe =  "HI of Dan"
            DownStatusIsSafe = False
            DownUnsafePawn = Temp_HC_Down_Value_Data
            DownDanPawnLocation = i - PosX+1
            break

    return UpStatusIsSafe,DownStatusIsSafe,UpUnsafePawn,DownUnsafePawn,UpDanPawnLocation,DownDanPawnLocation




def PawnsMovabilityChecker():
    pass


def CheckPawnRange(PawnName,PawnRequiredRange,RangeType):
    # print("PawnName: ",PawnName)
    # print("PawnRequiredRange: ",PawnRequiredRange)
    # print("RangeType: ",RangeType)
    if RangeType == "Strai":
        if PawnsRangeData[PawnName][0]>=str(PawnRequiredRange):
            return "Risk"
        else:
            return "Safe"
    

def CheckKingsSafety():
    localDoneOnce = False
    global CurrentlyCheckMated
    WKLeftSideSafe,WKRightSideSafe,WKLeftDanPawn,WKRightDanPawn,LeftSideDanPawnLocationInInt,RightSideDanPawnLocationInInt = HorizontalCheck(SavedWhiteKingPos)
    WKUpSideSafe,WKDownSideSafe,WKUpDanPawn,WKDownDanPawn,UpSideDanPawnLocationInInt,DownSideDanPawnLocationInInt = VerticalCheck(SavedWhiteKingPos)

    if WKLeftSideSafe == False:
        # print("White King should be Careful of : ", WKLeftDanPawn)
        if PawnsAbilityData[WKLeftDanPawn[1]][0]=="Y":
            # print("Be genuinely Careful of ",WKLeftDanPawn)
            if CheckPawnRange(WKLeftDanPawn[1],LeftSideDanPawnLocationInInt,"Strai") == "Risk":
                print("CHECKMATED ")
                CurrentlyCheckMated = True
                localDoneOnce = True
                
            else:
                CurrentlyCheckMated = False
        elif PawnsAbilityData[WKLeftDanPawn[1]][0] =="E":
            pass
    if WKRightSideSafe == False:
            # print("White King should be Careful of : ", WKRightDanPawn)
            if PawnsAbilityData[WKRightDanPawn[1]][0]=="Y":
                pass
                # print("Be genuinely Careful of ",WKRightDanPawn)
            elif PawnsAbilityData[WKRightDanPawn[1]][0] =="E":
                pass

    if WKUpSideSafe == False:
        # print("White King should be Careful of : ", WKLeftDanPawn)
        if PawnsAbilityData[WKUpDanPawn[1]][0]=="Y":
            # print("Be genuinely Careful of ",WKLeftDanPawn)
            if CheckPawnRange(WKUpDanPawn[1],UpSideDanPawnLocationInInt,"Strai") == "Risk":
                print("CHECKMATED ")
                CurrentlyCheckMated = True  
            else:
                    if not localDoneOnce:
                        CurrentlyCheckMated = False
        elif PawnsAbilityData[WKUpDanPawn[1]][0] =="E":
            pass
    if WKDownSideSafe == False:
        # print("White King should be Careful of : ", WKRightDanPawn)
        if PawnsAbilityData[WKDownDanPawn[1]][0]=="Y":
            pass
            # print("Be genuinely Careful of ",WKRightDanPawn)
        elif PawnsAbilityData[WKDownDanPawn[1]][0] =="E":
            pass



# print(HorizontalCheck("EE"))

while GameRunning !=False:
    SelectedBlock, AttackingBlock = AskForInput()
    UpdatePos(SelectedBlock, AttackingBlock)
    CheckKingsSafety()
    print(CurrentlyCheckMated)
    # print(CheckmatedDuration)
    if CurrentlyCheckMated:
        CheckmatedDuration +=1
    else:
        CheckmatedDuration = 0
    if CheckmatedDuration >= 2:
        # Data = PreviouslyData
        print("INVALID MOVE U HAVE YOUR KIND CHECKMATED: ")
        RevertChanges()
    Update()


# VerticalCheck("CE")
# print("Saved King: ",SavedWhiteKingPos)
# InputStringToNumberConverter("AA")
# InputNumberToStringConverter(int(input("Enter a Number: ")))
# HorizontalCheck("EE")
