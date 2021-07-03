
from pathlib import Path
import sys
import pandas as pd
from random import shuffle
import random
import numpy as np
import os
import re
from mutv1 import *

InputDir = r'D:\paradise\stuff\Essence\FS\all\sideInterestD\Sacred2'
dstDir = r'C:\FSJuction'
batchFSFile = r'D:\Developed\FSJunction\bodychehrFS.bat'

def getThisFile(sourceFile,parentDir):
    with open(r'D:\Developed\Automation\fnr\TargetDirs.opml','r') as fp:
        srcFileList = fp.readlines()
    # srcFileList.append(r'C:\bekar')
    for srcDir in srcFileList:
        dirP = Path(srcDir.rstrip())
        srcPath = dirP / parentDir / sourceFile
        # import pdb;pdb.set_trace()
        if srcPath.is_file():
            return srcPath
    return None



def getSourceFromDir(sourceFileName = 'Yummyh(91)',FromDir= r'D:\paradise\stuff\Essence\FS\DekhoKaiseChdvaRahiHai'):
    dstDirPath = Path(dstDir)  
    tkr = [x for x in Path(FromDir).rglob('*%s*.jpg' % sourceFileName)]
    listOfFoundFiles = []
    ExactDir = dstDirPath / sourceFileName / 'Body'
    for tk in tkr:
       if not re.search('.* @hudengi.*W1t81N.*',str(tk)):
          continue
       khr = re.search('(.*) @hudengi (.*) W1t81N (.*)',str(tk))
       dirName = re.search('(.*) @hudengi (.*) W1t81N (.*)',str(tk))[2]
       filename = re.search('(.*) @hudengi (.*) W1t81N (.*)',str(tk))[3]
       srcPath = getThisFile(filename,dirName)
       if srcPath is not None and not was_Copied(srcPath,ExactDir) :
          listOfFoundFiles.append(str(srcPath))
    if len(listOfFoundFiles) > 0:
        ExactDir.mkdir(parents=True,exist_ok=True)
        fileListCopy(listOfFoundFiles,str(ExactDir))
        Copied(listOfFoundFiles,ExactDir)
    # import pdb;pdb.set_trace()

def Copied(src_filepath,ExactDir):
    csvFilePath = ExactDir / 'copyRecords.csv'
    srcP = [Path(x).parent.name + '/' + Path(x).name for x in src_filepath]
    
    # import pdb;pdb.set_trace()
    if csvFilePath.is_file():
        df = pd.read_csv(str(csvFilePath))
        rf = pd.DataFrame(srcP, columns = ['srcFilePath'])
        df = df.append(rf)
    else:
        df = pd.DataFrame(srcP, columns = ['srcFilePath'])
    df.to_csv(str(csvFilePath))
    return
    

def was_Copied(src_filepath,DstDir):
    csvFilePath = DstDir / 'copyRecords.csv'
    # import pdb;pdb.set_trace()
    if not csvFilePath.is_file():
        return False
    srcP = Path(src_filepath).parent.name + '/' + Path(src_filepath).name
    df = pd.read_csv(str(csvFilePath))
    if not df[df['srcFilePath'] == srcP].empty:
        return True
    else:
        return False
        
    

def runFSjunction():
    dstDirPath = Path(dstDir)
    for fp in dstDirPath.rglob('*/Body/*.jpg'):
        os.chdir(fp.parent.parent)
        os.system(batchFSFile)
    
def updateChehre():
    ipPath = Path(InputDir)
    dstDirPath = Path(dstDir)
    InputDirSourceFileDir = r'D:\paradise\stuff\Essence\FS\all\sideInterestD'
    dirP = Path(InputDirSourceFileDir)
    for eachFile in ipPath.glob('*.jpg'):
        sourceFile = re.search('(.*) @hudengi (.*) W1t81N (.*)',eachFile.name)[3]
        mappedDevi = re.search('(.*) @hudengi (.*) W1t81N (.*)',eachFile.name)[1]
        srcPath = dirP / sourceFile
        targetFileP = dstDirPath / mappedDevi / 'Chehre'
        targetFileP.mkdir(parents=True,exist_ok=True)
        fileListCopy([str(srcPath)],str(targetFileP))

# updateChehre()
ipPath = Path(InputDir)

for eachFile in ipPath.glob('*.jpg'): 
    
    Filename = re.search('(.*) @hudengi (.*) W1t81N (.*)',eachFile.name)[1]
    getSourceFromDir(Filename)
runFSjunction()