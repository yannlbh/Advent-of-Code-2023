def OpenFile(fileName):
    f = open(fileName,"r")
    return f

def GetLineFromFile(file):
    return file.readlines()

def GetCombination(sequence):
    firstValue = "-1"
    lastValue = "-1"
    for c in sequence:
        if(c.isdigit()):
            if(firstValue == "-1"):
                firstValue = c
            lastValue = c
    if(firstValue == "-1"):
        return 0
    if(lastValue == "-1"):
        return int(firstValue+firstValue)
    return int(firstValue+lastValue)

def GetTotalValue(file):
    total = 0
    lines = GetLineFromFile(file)
    for line in lines:
        total += GetCombination(line)
    return total

def main():
    print(GetTotalValue(OpenFile("data.txt")))
    
if __name__ == '__main__':
    main()