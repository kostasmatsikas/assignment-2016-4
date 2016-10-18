__author__ = 'matsikaskonstantinos'

import argparse
import csv
import sys

class Node:
    def __init__(self, number):
        self.children = []
        self.parent = Node
        self.letter = Letter
        self.pathNumber = number
        self.trinaryValue = -1
        self.letter = ''
    def appendChild(self, newChild):
        self.children.append([newChild])
    def setLetter(self, letter):
        self.letter = letter
    def setChildren(self, children):
        self.children = (children)
    def setParent(parent):
        self.parent = parent
    def setTrinaryValue(self,trinaryValue):
        self.trinaryValue = trinaryValue

class Letter:
    def __init__(self, letter, frequency):
        self.letter = letter
        self.frequency = frequency
        self.node = Node
    def convertToNode(self):
        self.node = Node(self.frequency)
        self.node.setLetter(self.letter)
        return self.node

def loadLetters(filename):
    input_file = open(filename,'r')
    str = input_file.read()
    
    #print (str)
    input_file.close()


    letters = []
    for i in range(0,len(str)):
        letters += [str[i]]
    return letters 

def getUniqueLetters(letters):
    checkedLettersunique = []
    lettersunique = []
    
    for i in range(0, len(letters)):
        theLetter = letters[i]
        if(theLetter in checkedLettersunique):
            index = checkedLettersunique.index(theLetter)
            uniqueLetter = lettersunique[index]
            uniqueLetter.frequency = (uniqueLetter.frequency + 1)
        else:
            lettersunique.append(Letter(theLetter,1))
            checkedLettersunique.append(theLetter)
    return lettersunique

def letterBubblesort(letters):
    nums = list(letters)
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            if letters[j].frequency < letters[i].frequency:
                letters[j], letters[i] = letters[i], letters[j]
    return letters

def nodeBubblesort(letters):
    nums = list(letters)
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            if letters[j].pathNumber < letters[i].pathNumber:
                letters[j], letters[i] = letters[i], letters[j]
    return letters

def huffman(nodes):
    if(len(nodes) == 1):
        return nodes

    nodesToMerge = [nodes[0], nodes[1], nodes[2]]
    nodesSum = nodes[0].pathNumber + nodes[1].pathNumber + nodes[2].pathNumber
    mergedNode = Node(nodesSum)
    
    nodes[0].parent = mergedNode
    nodes[1].parent = mergedNode
    nodes[2].parent = mergedNode

    nodes[0].setTrinaryValue(0)
    nodes[1].setTrinaryValue(1)
    nodes[2].setTrinaryValue(2)
    
    mergedNode.setChildren(nodesToMerge)
    
    nodes.remove(nodes[0])
    nodes.remove(nodes[0])
    nodes.remove(nodes[0])

    nodes.append(mergedNode)
    nodes = nodeBubblesort(nodes)

    return huffman(nodes)

def getPath(node):
    result = []
    if(node.trinaryValue != -1):
        result = [node.trinaryValue]
        parentResult = getPath(node.parent)    
        result = result + parentResult

    return result

def getDnaCode(prevBase, currentTrit):
    if prevBase == 'A':
        if currentTrit == 0:
            return 'C'
        if currentTrit == 1:
            return 'G'
        else:
            return 'T'
    if prevBase == 'C':
        if currentTrit == 0:
            return 'G'
        if currentTrit == 1:
            return 'T'
        else:
            return 'A'
    if prevBase == 'G':
        if currentTrit == 0:
            return 'T'
        if currentTrit == 1:
            return 'A'
        else:
            return 'C'
    if prevBase == 'T':
        if currentTrit == 0:
            return 'A'
        if currentTrit == 1:
            return 'C'
        else:
            return 'G'

def getTrinaryDigit(prevBase, currentDna):
    if prevBase == 'A':
        if currentDna == 'C':
            return 0
        if currentDna == 'G':
            return 1
        else:
            return 2
    if prevBase == 'C':
        if currentDna == 'A':
            return 2
        if currentDna == 'G':
            return 0
        else:
            return 1
    if prevBase == 'G':
        if currentDna == 'A':
            return 1
        if currentDna == 'C':
            return 2
        else:
            return 0
    if prevBase == 'T':
        if currentDna == 'A':
            return 0
        if currentDna == 'C':
            return 1
        else:
            return 2

def encode(inputparam, outputparam, huffmanparam):
    text = loadLetters(inputparam)
    uniqueLetters = getUniqueLetters(text)

    if (len(uniqueLetters) % 2 == 0):
           uniqueLetters.append(Letter("",0))

    uniqueLetters = letterBubblesort(uniqueLetters)

    nodes = []
    for ltr in uniqueLetters:
        nodes.append(ltr.convertToNode())

    rootNode = huffman(nodes)

    for i in range(0, len(uniqueLetters)):
        printLetter = uniqueLetters[i].letter
        prineLetterTrinarypath = getPath(uniqueLetters[i].node)
        #print(printLetter)
        #print(prineLetterTrinarypath)

    print(text)
    #for i in range(0,(len(uniqueLetters))):
     #   print(uniqueLetters[i].letter)

    finalTrinaryPath = []
    for i in range(0,len(text)):
        for j in range(0,len(uniqueLetters)):
            if (text[i] == uniqueLetters[j].letter):
                finalTrinaryPath += getPath(uniqueLetters[j].node)

    prevBase = 'A'

    finalDnaCode = []
    for i in range (0,len(finalTrinaryPath)):
        finalDnaCode += getDnaCode(prevBase,finalTrinaryPath[i])
        prevBase = finalDnaCode[i]

    print(finalDnaCode)

    file = open(outputparam, 'a')
    file.write(''.join(finalDnaCode))
    file.close()

    csvLetters = []
    for i in range(0,len(uniqueLetters)):
        print(uniqueLetters[i].letter)
        print('---------')
        csvLetters.append(uniqueLetters[i].letter + ',' + ''.join(str(x) for x in getPath(uniqueLetters[i].node)))

    csv_file = open(huffmanparam, 'a')
    csv_file.write('\n'.join(csvLetters))
    csv_file.close()

def decode(inputparam, outputparam, huffmanparam):
    prevBase = 'A'
    primaryTrinaryCode = []
    userInput = loadLetters(inputparam)
    for i in range(0,len(userInput)):
        primaryTrinaryCode += getTrinaryDigit(prevBase,userInput)
        prevBase = userInput[i]

    print(primaryTrinaryCode)

    decode_dna=[]
    j = primaryTrinaryCode[0]
    for i in range (0,len(primaryTrinaryCode)):
            if (j in huffmanparam):
                decode_dna += huffmanparam
                j = primaryTrinaryCode[i]
            else:
                j += primaryTrinaryCode[i]

    file = open(outputparam, 'a')
    file.write(''.join(decode_dna))
    file.close()





parser = argparse.ArgumentParser()
parser.add_argument("input", help="inputparameter",
                    type=str)
parser.add_argument("output", help="outputparameter",
                    type=str)
parser.add_argument("huffman", help="huffmanparameter",
                    type=str)
parser.add_argument("-d","--decode", help="decoding",action="store_true", default=False)
args = parser.parse_args()


print (args.decode)

results = parser.parse_args()
print ('-------------')
print (results.decode_dna)
print ('-------------')
if(results.decode_dna == True):
    decode(results.input, results.output, results.huffman)
elif (len(sys.argv) > 2):
    encode(results.input, results.output, results.huffman)