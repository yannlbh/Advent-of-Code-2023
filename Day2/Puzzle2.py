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

def GetPowerOfLine(line):
    cubesMax = GetMaxNumCube(line)
    return cubesMax[0] * cubesMax[1] * cubesMax[2]

def GetTotalFromFile(file,numRC,numGC,numBC):
    total = 0
    lines = GetLineFromFile(file)
    for line in lines:
        total += GetPowerOfLine(line)
    return total

def main():
    print(GetTotalFromFile(OpenFile("data.txt"),12,13,14))
    
if __name__ == '__main__':
    main()