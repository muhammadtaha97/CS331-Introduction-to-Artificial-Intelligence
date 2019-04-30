#First simply I had to read a line and split it into two parts. One part to be gone for hMax and other to be assigned to
#string of Hmax + 1 digits. Then with the function call, we assume initially that no one is standing. Then we loop over
#the string to make up for every person, with increasing levels of hesitation, the first persons ofcourse (zeroth) index
#ones would have hesitation level zero so would stand up automatically, incrementing the number of people standing
#by the value at that specific index position and then if number of people standing is less than the number of required
#people standing than the minimum number of friends I should invite would be added to the required number according to
#hesitation level. It would then automatically increase the number of people standing as well, since I would be inviting
#frandsss


def standingOvation(hMax,string):
    frands = int(0)
    standing = int(0)
    for i in xrange(hMax + 1):
        if string[i] > "0":
            if standing < i:
                frands = frands + (i - standing)
                standing = i + int(string[i])
            else:
                standing = standing + int(string[i])
    return str(frands)




myfile = open("ovation.txt","r")
testcase = int(0)
string = ""
for line in myfile:
    if testcase == 0:
        testcase = testcase + 1
        continue
    wholeline = line.strip('\n').split(" ")
    hMax = int(wholeline[0])
    string = wholeline[1]
    testcase = testcase + 1
    print "Case " + str(testcase-1) + ": ",standingOvation(hMax,string)