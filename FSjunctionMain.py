
from pathlib import Path
import sys
import pandas as pd
from random import shuffle
import random
import numpy as np
import os
import re
from mutv1 import *
import shutil

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

def fileListCopy(fileList, DstDir):
    for fp in fileList:
        if (Path(DstDir) / Path(fp).name).is_file():
            return
        if not Path(fp).is_file():
            print('src file not found', fp)
            continue
        shutil.copy(fp, DstDir)

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
          copyIn = ExactDir / srcPath.parent.name
          copyIn.mkdir(parents=True,exist_ok=True)
          fileListCopy([str(srcPath)],str(copyIn))
    if len(listOfFoundFiles) > 0:
        # copyIn = ExactDir / 
        # ExactDir.mkdir(parents=True,exist_ok=True)
        # fileListCopy(listOfFoundFiles,str(ExactDir))
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
        
def DeleteBekar():
    ipPath = Path(InputDir)
    dstDirPath = Path(dstDir)
    # dstDirPath = Path(dstDir)
    # InputDirSourceFileDir = r'D:\paradise\stuff\Essence\FS\all\sideInterestD'
    # dirP = ipPath.parent
    for fp in dstDirPath.rglob('*/Chehre/*.jpg'):
        # import pdb;pdb.set_trace() 
        associatedFiles = [x for x in ipPath.glob('*W1t81N %s.jp*g' % fp.stem)]
        if associatedFiles == []:
            print('deleting: ',fp)
            fp.unlink()
    for fpp in dstDirPath.rglob('*/Chehre*'):
        # fpp = fp.parent.parent / 'Chehre'
        if [x for x in fpp.glob('*.jpg')] == []:
            shutil.rmtree(fpp.parent)
        

def runFSjunction():
    dstDirPath = Path(dstDir)
    batchCmd = r'"C:\Users\HP\Miniconda3\scripts\activate.bat" && conda activate "faceswap" && python "D:\Developed\FaceSwapExperimental\FSBodyMajor.py" @slut@ @pavitra@ @resultFolder@ 5'
    batchCmd = batchCmd.replace('@resultFolder@', '"C:\\Games\\sacred2"')
    for fp in dstDirPath.rglob('*/Body/*/'):
        if fp.is_file():
            continue
        print(fp)
        # os.chdir(fp.parent.parent.parent)
        for dirs in fp.parent.iterdir():
            faceP = dirs.parent.parent / 'Chehre'
            ubatchCmd = batchCmd.replace('@pavitra@','"%s"' %  str(faceP))
            if not dirs.is_dir() or dirs.name == 'done':
                continue
            ubatchCmd = ubatchCmd.replace('@slut@','"%s"' % str(dirs))
            testBatP = dirs / 'testRun.bat'
            with open(testBatP, 'w') as batfp:
                batfp.write(ubatchCmd)
            
            # os.system(ubatchCmd)
            os.system('"%s"' % str(testBatP))
            # import pdb;pdb.set_trace()
            shutil.rmtree(dirs)
    
def updateChehre():
    ipPath = Path(InputDir)
    dstDirPath = Path(dstDir)
    # InputDirSourceFileDir = r'D:\paradise\stuff\Essence\FS\all\sideInterestD'
    dirP = ipPath.parent
    for eachFile in ipPath.glob('*.jpg'):
        sourceFile = re.search('(.*) @hudengi (.*) W1t81N (.*)',eachFile.name)[3]
        mappedDevi = re.search('(.*) @hudengi (.*) W1t81N (.*)',eachFile.name)[1]
        srcPath = dirP / sourceFile
        targetFileP = dstDirPath / mappedDevi / 'Chehre'
        targetFileP.mkdir(parents=True,exist_ok=True)
        fileListCopy([str(srcPath)],str(targetFileP))

updateChehre()
DeleteBekar()
ipPath = Path(InputDir)

for eachFile in ipPath.glob('*.jpg'): 
    
    Filename = re.search('(.*) @hudengi (.*) W1t81N (.*)',eachFile.name)[1]
    getSourceFromDir(Filename)
runFSjunction()