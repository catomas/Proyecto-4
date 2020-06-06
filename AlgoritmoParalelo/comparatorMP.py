from numpy import *
from time import time
from multiprocessing import Pool, cpu_count

def compare():
    text1 = open("text1.txt","r")
    text2 = open("text2.txt","r")

    tiempo_inicial = time() 
    comparison = textDiff(text1,text2)
    tiempo_final = time() 

    tiempo_ejecucion = tiempo_final - tiempo_inicial
    print ('El tiempo de ejecucion fue:',tiempo_ejecucion)
    
def textDiff(text1, text2):

    text1Arr = [linea.strip() for linea in text1]
    text1Arr = [linea for linea in text1Arr if linea != '']
    text2Arr = [linea.strip() for linea in text2]
    text2Arr = [linea for linea in text2Arr if linea != '']

    rankings = rankingTables(text1Arr,text2Arr)
    return rankings
def rankingTables(text1Arr, text2Arr):
    pool = Pool()
    paragraphTuples = list()
    for paragraph1 in text1Arr:
        paragraphTuples.append((paragraph1, text2Arr)) 
    return pool.map(compareParagraph, paragraphTuples)

def compareParagraph(paragraphTuple):
    return doCompareParagraph(paragraphTuple[0], paragraphTuple[1])
    
def doCompareParagraph(paragraph1, paragraphs):
    p1 = paragraph1.split(' ')
    p1 = [linea for linea in p1 if linea != '']
    ranking = []
    for paragraph2 in paragraphs:
        p2 = paragraph2.split(' ')
        p2 = [linea for linea in p2 if linea != '']
        lcsMatrix = lcsMatrixAlgorithm(p1,p2)
        coincidences = lcsMax(lcsMatrix)
        differences = abs((len(p1) - len(p2)))
        ranking.append([coincidences,differences])
    if len(ranking) > 0:
        sortRanking(ranking)
    return ranking        

def mayorCoin(elem):
    return elem[1]

def sortRanking(ranking):
    ranking.sort(reverse=True,key=mayorCoin,)
    
def lcsMatrixAlgorithm(text1, text2):
    lcsMatrix = []
    for i in range(0,len(text2) + 1):
        lcsMatrix.insert(i,[0]*(len(text1)+1))
    for i in range(1,len(lcsMatrix)):
        for j in range(1,len(lcsMatrix[i])):
            if text1[j-1] == text2[i-1]:
                lcsMatrix[i][j] = lcsMatrix[i - 1][j - 1] + 1
            else:
                lcsMatrix[i][j] = max(lcsMatrix[i][j - 1], lcsMatrix[i - 1][j])
    return lcsMatrix

def lcsMax(lcsMatrix):
    row = len(lcsMatrix)-1 
    col = len(lcsMatrix[row])-1
    return lcsMatrix[row][col]


    

compare()
