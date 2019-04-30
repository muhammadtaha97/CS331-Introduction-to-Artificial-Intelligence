#Basically whatever number Tonton sheep thinks, I will compare the string version of that number with a fixed string
#containing all the digits from 0-9. If a digit is found in Tonton number string then that number is deleted from our
#fixed string. Now the loop will only break if all the digits in the fixed string are removed that is its length would
#become zero. This would imply that Tonton has now thought of every digit. For the base case, i.e 0, the loop would have
#never stopped since anything multiplied by 0 would be 0 so that was handled before, since this leads to INSOMNIA :)
def sheep(number):
    fixedstr = '0123456789'
    numberplus1 = int(2)
    if number == 0:
        return "IMSOMNIA"
    while True:
        numberstr = str(number)
        for x in xrange(len(fixedstr)-1,-1,-1):
            if fixedstr[x] in numberstr:
                fixedstr=fixedstr.replace(fixedstr[x],'')
        if len(fixedstr)==0:
            break
        number = origno * numberplus1
        numberplus1 = numberplus1 + 1
    return number

filename = "sheep.txt"
myfile = open(filename,"r")
testcase = int(0)
for line in myfile:
    number = int(line.strip())
    if testcase == 0:
        testcase = testcase + 1
        continue
    origno = int(number)
    testcase = testcase + 1
    print number, "Case #", testcase-1, sheep(number)