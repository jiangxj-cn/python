import os,os.path,re

def Reduce(sourceFolder,targetFile):
    tempData={}
    p_re=re.compile(r'(.*?)(\d{1,}$)',re.IGNORECASE)
    for root,dirs,files in os.walk(sourceFolder):
        for fil in files:
            if fil.endswith('_map.txt'):
                sFile=open(os.path.abspath(os.path.join(root,fil)),'r')
                dataLine=sFile.readline()

                while dataLine:
                    subdata=p_re.findall(dataLine)
                    if subdata[0][0] in tempData:
                        tempData[subdata[0][0]]+=int(subdata[0][1])
                    else:
                        tempData[subdata[0][0]]=int(subdata[0][1])
                    dataLine=sFile.readline()
                sFile.close()
    tList=[]
    for key,value in sorted(tempData.items(),key=lambda k:k[1],reverse=True):
        tList.append(key+" "+str(value)+'\n')
    tFilename=os.path.join(sourceFolder,targetFile+"_reduce.txt")
    tFile=open(tFilename,'a+')
    tFile.writelines(tList)
    tFile.close()
if __name__=="__main__":
    Reduce("map","reduce")
