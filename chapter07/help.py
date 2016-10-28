import sys, pickle, shelve

def signFile():

    myFile=shelve.open('document')

    myFile['Player1']='100'
    myFile['Player2']='100'
    myFile['Player3']='100'

    myFile.close()

def addRecord(userName):

    myFile=shelve.open('document')
    record=1001
    myFile[userName]=record

def readRecords():

    myFile=shelve.open('document')
    for name in myFile:
        print(name, myFile[name])

def writeData(filename, name, record):

    file=open(filename, 'a')
    file.write(name)
    file.write(record)    
    file.close
    
def zapolniFileTxt():
    for i in range(4):
          name='Player'+str(i)+'\n'
          record=str(i)+'00'+'\n'
          writeData('doc1.txt', name,record)

def readDataTxt(file):
    file=open(file, 'r')

    name=' '

    print('\n___SCORES___\n')
    while name:
        name=file.readline()
        score=file.readline()

        print(name, score)
    file.close

writeData('doc1.txt', 'player1\n', '500\n')
#writeScoreTxt('doc1.txt', 'Yar', '400')
readDataTxt('doc1.txt')
