__author__ = 'matsikaskonstantinos'

import argparse
import csv

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

def getTritValue():
    return '01201201201201210'

def getDnaCode(prevBase,currentTrit):
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


filename = 'mytext.txt'

text = loadLetters(filename)
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

#print(text)
#for i in range(0,(len(uniqueLetters))):
 #   print(uniqueLetters[i].letter)

finalTrinaryPath = []
for i in range(0,len(text)):
    for j in range(0,len(uniqueLetters)):
        if (text[i] == uniqueLetters[j].letter):
            finalTrinaryPath += getPath(uniqueLetters[j].node)

print(finalTrinaryPath)
prevBase = 'A'

finalDnaCode=[]
for i in range (0,len(finalTrinaryPath)):
    finalDnaCode += getDnaCode(prevBase,finalTrinaryPath[i])
    prevBase = finalDnaCode[i]

print(finalDnaCode)