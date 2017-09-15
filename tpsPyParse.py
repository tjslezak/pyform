import pandas as pd
import numpy as np

def pyTPStoDict(tpsPath):
    tpsFile = open(tpsPath, 'r')
    tpsDict = {'id':[], 'image':[], 'x':[], 'y':[], 'lm':[], 'scale': []}
    numLand = 0
    for line in tpsFile:
        if line[0] == 'L':
            numLand = int(line.split('=')[1])
            temp = [int(line.split('=')[1])]
            tpsDict['lm'].extend([item for item in temp for i in range(numLand)])
        elif line[:2] == 'IM':
            imageFu = line.split('=')[1]
            imageFu.rstrip()
            imageFu = imageFu.split('.')[0]
            temp = [imageFu]
            tpsDict['image'].extend([item for item in temp for i in range(numLand)])
        elif line[:2] == 'ID':
            temp = [int(line.split('=')[1])]
            tpsDict['id'].extend([item for item in temp for i in range(numLand)])
        elif line[0] == 'S':
            temp = [float(line.split('=')[1])]
            tpsDict['scale'].extend([item for item in temp for i in range(numLand)])
        else:
            tempxy = line.split(' ')
            tpsDict['x'].append(float(tempxy[0]))
            tpsDict['y'].append(float(tempxy[1]))
    tpsFile.close()
    return tpsDict

def main():
    tpsFilePath = "exaSpec.TPS"
    nativePythonTPS = pyTPStoDict(tpsFilePath)
    pandasTPS = pd.DataFrame(nativePythonTPS)
    print(pandasTPS)

if __name__ == "__main__":
    main()
