def OpenFile(fileName):
    f = open(fileName,"r")
    return f

def GetLineFromFile(file):
    return file.readlines()

def ReplaceNumStrWithNum(sequence):
    replaceDict = {'one' : 'on1e', 'two' : 'tw2o', 'three' : 'thr3e','four': 'fo4ur', 'five':'fi5ve','six': 'si6x','seven': 'sev7en','eight' : 
'ei8ght','nine':'ni9ne'}
    for key,value in replaceDict.items():
        sequence = sequence.replace(key,value)
    return sequence

def GetCombination(sequence):
    firstValue = "-1"
    lastValue = "-1"
    sequence = ReplaceNumStrWithNum(sequence)
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