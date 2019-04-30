import numpy as np
import time
import sys




def readtrain(trainfile):
	trainfile = trainfile+ ".txt"
	trainfile = open(trainfile, "r")
	trainfile = trainfile.readlines()

	i = int(0)
	while (i < 80):
		trainfile[i] = trainfile[i].replace(",","")
		trainfile[i] = trainfile[i].replace("\r","")
		trainfile[i] = trainfile[i].replace("\n","")
		i = i+1

	return trainfile
        
def readtest(testfile):
	testfile = testfile+ ".txt"
	testfile = open(testfile, "r")
	testfile = testfile.readlines()

	i = int(0)
	while (i < 187):
		testfile[i] = testfile[i].replace(",","")
		testfile[i] = testfile[i].replace("\r","")
		testfile[i] = testfile[i].replace("\n","")
		i = i+1
	#print testfile
	return testfile



def train_and_test(trainfile,testfile):
	print "#####################################################################"
	print(" ")
	print("Starting to Train on 80 data points . . .")
	print("                                         ")
	inputtrain = readtrain(trainfile)
	#print (inputtrain)
	normalone = []
	normalzero = []
	abnormalone = []
	abnormalzero = []

	for j in range(1,23):
		normal_ones = int(0)
		normal_zeroes = int(0)
		for i in range(0,40):
			if int(inputtrain[i][j]) == 1:
				normal_ones = normal_ones + 1
			else:
				normal_zeroes = normal_zeroes + 1
		normalone.append(float(normal_ones)/float(40))
		normalzero.append(float(normal_zeroes)/float(40))

	for j in range(1,23):
		abnormal_ones = int(0)
		abnormal_zeroes = int(0)	
		for i in range(41,80):
			if int(inputtrain[i][j]) == 1:
				abnormal_ones = abnormal_ones + 1
			else:
				abnormal_zeroes = abnormal_zeroes + 1
		abnormalone.append(float(abnormal_ones)/float(40))
		abnormalzero.append(float(abnormal_zeroes)/float(40))

	normalone = np.array(normalone)
	normalzero = np.array(normalzero)
	abnormalone = np.array(abnormalone)
	abnormalzero = np.array(abnormalzero)
	#print normalone
	#print normalzero
	#print abnormalone
	#print abnormalzero

	normaloneprob = np.prod(normalone)
	normalzeroprob = np.prod(normalzero)
	abnormaloneprob = np.prod(abnormalone)
	abnormalzeroprob = np.prod(abnormalzero)
	print"             "
	print "Testing on 187 data point..."

	#print normaloneprob
	#print normalzeroprob
	#print abnormaloneprob
	#print abnormalzeroprob
	inputtest = readtest(testfile)

	normalone = []

	for i in range(0,187):
	    normallist1 = []
	    for j in range(1,23):
	        if int(inputtest[i][j]) == 0:
	        	normallist1.append(1-normaloneprob)
	        else:
	            normallist1.append(normaloneprob)
	    normallist1 = np.array(normallist1)
	    normallist1 = np.prod(normallist1) 
	    normalone.append(normallist1)

	normalzero = []

	for i in range(0, 187):
	    normallist2 = []
	    for j in range(1, 23):
	        if int(inputtest[i][j]) == 0:
	        	normallist2.append(1 - normalzeroprob)
	        else:
	            normallist2.append(normalzeroprob)
	    normallist2 = np.array(normallist2)
	    normallist2 = np.prod(normallist2)
	    normalzero.append(normallist2)

	abnormalone=[]

	for i in range(0, 187):
	    abnormallist1 = []
	    for j in range(1, 23):
	        if int(inputtest[i][j]) == 0:
	        	abnormallist1.append(1 - abnormaloneprob)	            
	        else:
	            abnormallist1.append(abnormaloneprob)
	    abnormallist1 = np.array(abnormallist1)
	    abnormallist1 = np.prod(abnormallist1)
	    abnormalone.append(abnormallist1)

	abnormalzero=[]

	for i in range(0, 187):
	    abnormallist2 = []
	    for j in range(1, 23):
	        if int(inputtest[i][j]) == 0:
	        	abnormallist2.append(1 - abnormalzeroprob)
	        else:
	        	abnormallist2.append(abnormalzeroprob)	            
	    abnormallist2 = np.array(abnormallist2)
	    abnormallist2 = np.prod(abnormallist2)
	    abnormalzero.append(abnormallist2)

	correct = int(0)

	for i in range(0,187):
	    if ((normalone[i] > abnormalone[i]) or (normalzero[i] > abnormalzero[i])) and (inputtest[i][0] == "1") :
	    	correct = correct + 1
	accuracy = float(correct/187.0)

	return accuracy


def main():
	trainfile = sys.argv[1]
	testfile =  sys.argv[2]
	starttime = time.time()
	accuracy = train_and_test(trainfile,testfile)
	endtime = time.time()
	totaltime = endtime - starttime
	print "Total time taken = " ,float(totaltime), "seconds "
	print "  "
	print "Total Accuracy := ",float(accuracy*100) , "%"
	print " "
	print "#####################################################################"
   	
	
	

if __name__ == '__main__':
    main()   
