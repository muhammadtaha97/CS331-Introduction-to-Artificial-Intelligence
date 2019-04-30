def LongestPalindrome(palindstring):
    largestpalin = ""
    currlargest = int(0)
    currentpalin=""
    longestpal = int(0)
    palinlength = len(palindstring)
    i = int(0)
    end = int(0)
    
    for i in range(palinlength):
        for j in range(palinlength-1,i,-1):
            if (palindstring[i]== palindstring[j]):
                for n in range(i,j+1):
                    if palindstring[n] != palindstring[j-end]:
                        break
                    else:
                        currlargest = currlargest + 1
                        currentpalin = currentpalin+str(palindstring[n])
                        if longestpal < currlargest:
                            longestpal = currlargest
                            largestpalin = currentpalin
                    end=end+1
            currlargest = 0
            currentpalin =""
            end = 0
    if longestpal > 0:
        print "Longest Palindrome: \"" + largestpalin + "\" of length : ", longestpal
    else:
        if (palinlength != 1):
            print "Possible Palindromes are : "
        for counter in range(palinlength):
            print "Longest Palindrome: \"" + palindstring[counter] + "\" of length : 1"

palinstring = ""
print("Please enter a string or sequence : ")
palinstring = str(raw_input())
LongestPalindrome(palinstring)