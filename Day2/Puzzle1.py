def OpenFile(fileName):
    f = open(fileName,"r")
    return f

def GetLineFromFile(file):
    return file.readlines()

def GetMaxNumCube(line):
    line = line.split()
    index = 2
    cubesMax = [-1,-1,-1]
    while(index+1 <= len(line)):
        val = int(line[index])
        if("red" in line[index+1]):
            if(val > cubesMax[0]):
                cubesMax[0] = val
        if("green" in line[index+1]):
            if(val > cubesMax[1]):
                cubesMax[1] = val
        if("blue" in line[index+1]):
            if(val > cubesMax[2]):
                cubesMax[2] = val
        index += 2
    return cubesMax

def CheckIsPossibleLine(line,numRC,numGC,numBC):
    cubesMax = GetMaxNumCube(line)
    if(cubesMax[0] > numRC):
        return False
    if(cubesMax[1] > numGC):
        return False
    if(cubesMax[2] > numBC):
        return False
    return True

def CheckFilePossible(file,numRC,numGC,numBC):
    total = 0
    index = 1
    lines = GetLineFromFile(file)
    for line in lines:
        if(CheckIsPossibleLine(line,numRC,numGC,numBC)):
            total += index
        index += 1
    return total

def main():
    print(CheckFilePossible(OpenFile("data.txt"),12,13,14))
    
if __name__ == '__main__':
    main()