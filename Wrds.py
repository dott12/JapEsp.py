import csv
import random
from random import randint

def quitarNones():
    for i in range(len(japList)):
        if japList[i] == "none":
            japList[i] = hiraganaList[i]

def mergeHiraKanji():
    for i in range(len(japList)):
            japList[i] = japList[i]+" ("+hiraganaList[i]+")"

def startTest():
    while 1 < 2:

        value = randint(0, len(japList)-1)  ##valor random para que la palabra sea random

        print(japList[value] + ": ")
        word = input("Significado: ")

        if (word == espList[value]):
            print("Correcto!")
        else:
            print("*********************Incorrecto, es: " + espList[value] + " ("+hiraganaList[value]+")")

def hiratest():
    while 1 < 2:

        value = randint(0, len(japList)-1)  ##valor random para que la palabra sea random

        print(japList[value] + ": ")
        word = input("Hiragana: ")

        if (word == hiraganaList[value]):
            print("Correcto!")
        else:
            print("*********************Incorrecto, es: " + hiraganaList[value])

japList = []
hiraganaList=[]
espList = []

##Se abre el csv
with open('WordsDic.csv','r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

#####Programa

    level = input("Qué nivel probarás?: ")



##Aqui se llenan las listas que se van a usar
    for line in csv_reader:
        ##print (line[5])

        if line[5] == str(level):
            espList.append(line[2])
            japList.append(line[3])
            hiraganaList.append(line[4])


    quitarNones()


    opcion = input("Qué quieres probar? \n1.Japones->Español \n2.Kanji->Hiragana \n")

    if opcion == "1":
        Hiragana = input("Quieres mostrar hiragana? (si/no)")
        if Hiragana == "no":
            startTest()
        else:
            mergeHiraKanji()
            startTest()

    if opcion == "2":
        hiratest()


##segmento de codigo si no quiere mostrar hiragana


    ##for x in japList:
       ## print(x)

    ##print(hiraganaList)





