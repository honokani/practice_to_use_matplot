import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot  as plt
import random
import os 

dirPath = os.path.dirname(os.path.realpath(__file__))


def decideLine(xs, angle, shift):
    y = (np.sin( list(map(lambda x: (x+np.random.randn())/8, xs)) ) * 30 + angle) * xs / 150 + 50 + shift
    return y

def spreadPoint(sx, gn, gs, tgts):
    xs = []
    for tgt in tgts:
        for exp in (np.random.randn(gn)*sx*gs):
            xs.append(tgt + exp)

    return xs

def plotPoint(sx, sy, n):
    plt.axis([0, sx, 0, sy])
    groupNum = 0
    groupDence = 0
    groupSize = sx
    particleShape = ""
    particleAlpha = 0.1
    progressiveLines = [ [0,0]
                       # right-up
                       , [25,0]
                       , [25,5]
                       , [50,0]
                       , [50,5]
                       , [50,-5]
                       , [25,25]
                       , [25,-25]
                       # right-down
                       , [-25,0]
                       , [-25,5]
                       , [-50,0]
                       , [-50,5]
                       , [-50,-5]
                       , [-25,25]
                       , [-25,-25]
                       ]

    if n==1 :
        groupNum = 3
        groupDence = 24
        groupSize = 0.02
        particleShape = "."
        progressiveLines = random.sample(progressiveLines, 1)
    elif n==2 :
        for i in range(4):
            plotPoint(sx,sy,1)
        groupNum = 2
        groupDence = 60
        groupSize = 0.04
        particleShape = "o"
        progressiveLines = random.sample(progressiveLines, 2)
    elif n==3 :
        for i in range(2):
            plotPoint(sx,sy,2)
        groupNum = 3
        groupDence = 60
        groupSize = 0.04
        particleShape = "o"
        progressiveLines = random.sample(progressiveLines, 5)
    else :
        progressiveLine = []

    for pl in progressiveLines:
        x = np.random.rand(groupNum) * sx
        x = spreadPoint(sx, groupDence, groupSize, x)
        y = decideLine(x, *pl)
        y = list(map(lambda i: i+np.random.randn()*sy*groupSize ,y))
        plt.plot(x, y, particleShape, alpha=particleAlpha, color="blue")

def addNoise():
    print("WIP noise")

def controlSaveDir(i):
    labeledDirs = []

    picDirName = "pics"
    picDir = os.path.join(dirPath, picDirName)
    if not os.path.exists(picDir):
        os.makedirs(picDir)
    for j in range(i):
        labeledDirName = str(j)
        labeledDir = os.path.join(picDir, labeledDirName)
        if not os.path.exists(labeledDir):
            os.makedirs(labeledDir)
        labeledDirs.append(labeledDir)

    return labeledDirs


def snapImage(p, picNum):
    ext = ".png"
    picFile = os.path.join(p, str(picNum) + ext)
    plt.savefig(picFile)
    picNum += 1

def main():
    # fix screen size
    size_x = 100
    size_y = 100

    totalLabelNum = 4
    labeledDirs = controlSaveDir(totalLabelNum)

    picNum = 0
    for i in range(totalLabelNum):
        # plot points
        plotPoint(size_x, size_y, i)
        addNoise()
        # snap image
        snapImage(labeledDirs[i], picNum)
        # clear screen
        plt.clf()

    plt.show()

main()

