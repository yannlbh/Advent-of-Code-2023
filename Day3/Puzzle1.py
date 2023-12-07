def OpenFile(fileName):
    f = open(fileName,"r")
    return f

def GetLineFromFile(file):
    return file.readlines()

def CreateLine(sequence):
    lstLine = []
    for c in sequence:
        lstLine.append(c)
    return lstLine

def CreateTab(lines):
    tab = []
    for line in lines:
        tab.append([x for x in line])
    return tab

def CheckIfSymbol(col,row,tab,radius):
    lstSymbol = ["*","%","/","#","-","+","=","@","&","$"]
    for i in range(row - 1, row + 2):
        for j in range(col - radius , col + 2):
            if ((i >= 0 and i < len(tab)) and (j >= 0 and j < len(tab[i]))):
                for symbole in lstSymbol:
                    if(tab[i][j] == symbole):
                        return True
    return False

def CalculateTotNumber(lst):
    tot = 0
    for num in lst:
        tot += int(num)
    return tot

def GetNumberLine(line,row,tab):
    lstNumber = []
    number = ""
    col = 0
    for c in line:
        if(c.isdigit()):
            number += c
        else:
            if(number!="" and CheckIfSymbol(col-1,row,tab,len(number))):
                lstNumber.append(number)
            number = ""              
        col += 1
    return CalculateTotNumber(lstNumber)
        
def GetTotal(file):
    lines = GetLineFromFile(file)
    tab = CreateTab(lines)
    row = 0
    tot = 0
    for line in tab:
        tot += GetNumberLine(line,row,tab)
        row += 1
    return tot

def main():
    print(GetTotal(OpenFile("data.txt")))
    
if __name__ == '__main__':
    main()