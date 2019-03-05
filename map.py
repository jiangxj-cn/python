import os,os.path,re

def Map(sourceFolder,tgtFolder):

    for root,dirs,files in os.walk(sourceFolder):
        for fil in files:
            if fil.endswith('_piece.txt'):
                sFile=open(os.path.abspath(os.path.join(root,fil)),'r')
                dataLine=sFile.readline()
                tempData={}
                if not os.path.isdir(tgtFolder):
                    os.mkdir(tgtFolder)
                while dataLine:
                    p_re=re.compile(r'(GET|POST)\s(.*?)\s',re.IGNORECASE)
                    match=p_re.findall(dataLine)
                    if match:
                        visitUrl=match[0][1]
                        if visitUrl in tempData:
                            tempData[visitUrl]+=1
                        else:
                            tempData[visitUrl]=1
                    dataLine=sFile.readline()
                sFile.close()
                tList=[]
                for key,value in sorted(tempData.items(),key=lambda k:k[1],reverse=True):
                    tList.append(key+" "+str(value)+'\n')
                tFilename=os.path.join(tgtFolder,os.path.split(fil)[1]+"_map.txt")
                tFile=open(tFilename,'a+')
                tFile.writelines(tList)
                tFile.close()
if __name__=="__main__":
    Map("access","map")