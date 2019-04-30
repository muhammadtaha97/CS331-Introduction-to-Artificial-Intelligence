import numpy as np
import time
import sys
def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

def trainread(traintxt):

    traintxt = open(traintxt, "r")
    list = []

    i = int(0)
    while (i < 60000):
        matrix = ""
        j = int(0)
        while (j < 44):
            line = traintxt.readline()
            line = line.strip("[")
            line = line.replace("]", "")
            matrix = matrix + line
            j = j + 1
        matrix = matrix.split()
        matrix = map(int, matrix) #To convert to integer
        list.append(matrix)
        i = i + 1

    return list

def testread(testtxt):

    traintxt = open(testtxt, "r")
    list = []

    i = int(0)
    while (i < 10000):
        matrix = ""
        j = int(0)
        while (j < 44):
            line = traintxt.readline()
            line = line.strip("[")
            line = line.replace("]", "")
            matrix = matrix + line
            j = j + 1
        matrix = matrix.split()
        matrix = map(int, matrix) #To convert to integer
        list.append(matrix)
        i = i + 1

    return list

def testlabels(testlabelfile):
    testlabel = open(testlabelfile, "r")
    list = []

    for line in testlabel:
        list.append(int(line))

    return list

def trainlabels(trainlabelfile):
    trainlabel = open(trainlabelfile, "r")
    list = []

    for line in trainlabel:
        list.append(int(line))

    return list

def train(traintext, trainlabelfile, rate):
    #Starting time taken to train
    
    print("Okay lets start to train this neural network")
    starttime = time.time()

    inputlayer = trainread(traintext)
    trainlabel = trainlabels(trainlabelfile)

    learningRate = rate

    #Finishing time
    endtime = time.time()
    totaltime = endtime - starttime

    print ("Training finished. Total time taken to train this neural network is : " , float(totaltime))


def test(testtext, testlabels, netweighttxt):
    print ("Now for the testing part : ")
    inputtest = testread(testtext)
    labeltest = testlabel(testlabels)

def main():
    choice = sys.argv[1]
    textfile = sys.argv[2]
    labels = sys.argv[3]
    rateornetweights = sys.argv[4]

    
    if (choice == "train"):
        train(textfile, labels, float(rateornetweights))
    elif(choice == "test"):
        test(textfile, labels, rateornetweights)

if __name__ == '__main__':
    main()   


    






def sigmoidprime(z):
    return (sigmoid(z) * (1 - sigmoid(z)))