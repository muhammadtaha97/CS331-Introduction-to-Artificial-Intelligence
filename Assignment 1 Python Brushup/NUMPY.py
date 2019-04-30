import numpy as np

inputData = [[0, 0, 1],
             [0, 1, 1],
             [1, 0, 1],
             [1, 1, 1]]
print("Input as single line list (we do not want the input to look like this):")
print(inputData)

a = np.array(inputData)
print "The output for task 1 is : " 
print a

print "TASK2 : "
threeby1= np.random.random((3,1))
fiveby2 = np.random.random((5,2))

print "ThreebyOne : "
print threeby1

print "five by two : "
print fiveby2

print "Task 3 : "

c,d = np.hsplit(inputData,(2,1))
print c
print d

print "Task 4: "
fivebyfour = np.random.random((5,4))
fourbyone = np.random.random((4,1))

matrixproduct = fivebyfour.dot(fourbyone)
print matrixproduct