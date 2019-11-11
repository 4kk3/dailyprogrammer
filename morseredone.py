import string
import random

def smorse(wordtokonvert):
    wordtokonvert = list(wordtokonvert)
    wordtokonvertbackup = wordtokonvert
    finnishedword = ""
    finnishedwordmorse = []
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    morsealphabet = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    while len(wordtokonvert) != 0:
        testletter = ""
        if len(wordtokonvert) == 1:
            randomindex = 1
        elif len(wordtokonvert) < 5:
            randomindex = random.randrange(len(wordtokonvert) + 1)
        else:
            randomindex = random.randrange(6)
        for i in range (randomindex):
            testletter += wordtokonvert[i]
        if testletter in morsealphabet:
            finnishedwordmorse += [testletter]
            del wordtokonvert[0:randomindex]
    for i1 in range (len(finnishedwordmorse)):
        for i2 in range (len(morsealphabet)):
                if finnishedwordmorse[i1] == morsealphabet[i2]:
                    finnishedword+= alphabet[i2]
    return finnishedword 

def main():
    smorsevarde = ""
    while smorsevarde != "sos":
        smorsevarde = smorse("...---...")
        print(smorsevarde)
    print("-------")
