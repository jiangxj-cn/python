import os,os.path,time

def FileSplit(sourceFile,TgtFolder):
    sFile=open(sourceFile,'r')
    number=1000
    dataLine=sFile.readline()
    tempData=[]
    fileNum=1
    if not os.path.isdir(TgtFolder):
        os.mkdir(TgtFolder)
    while dataLine:
        for row in range(number):
            tempData.append(dataLine)
            dataLine=sFile.readline()
            if not dataLine:
                break
        tFileName=os.path.join(TgtFolder,os.path.split(sourceFile)[1]+str(fileNum)+"_piece.txt")
        tFile=open(tFileName,'a+')
        tFile.writelines(tempData)
        tFile.close()
        tempData=[]
        print(tFileName+" 创建于："+str(time.ctime()))
        fileNum+=1
    sFile.close()
if __name__=="__main__":
    FileSplit("access.log","access")