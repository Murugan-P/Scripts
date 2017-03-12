import os
import zipfile
import shutil

#set numbers
dogValid=1000
catValid=1000
dogSampleTrain=80
catSampleTrain=80
dogSampleValid=20
catSampleValid=20

#create directories
dir = "~/nbs/asgmnt1/data/dogscats"

dirList = ['/test1/','/valid/','/valid/dogs/','/valid/cats/','/sample/','/sample/train/','/sample/train/dogs/','/sample/train/cats/',
                '/train/','/train/dogs/','/train/cats/','/sample/valid/', '/sample/valid/dogs/', '/sample/valid/cats/']

for i in range (0, len(dirList)):
    if i<len(dirList):
        if not os.path.exists(os.path.dirname(dir+dirList[i])):
            os.makedirs(os.path.dirname(dir+dirList[i]))
    else:
        if not os.path.exists(os.path.dirname(dir+dirList[-1])):
            os.makedirs(os.path.dirname(dir+dirList[-1]))

#unzip files in proper directories
files = os.listdir("~/nbs/asgmnt1/")
for f in files:
    if (f.startswith("Test") or f.startswith("test")):
        zip_ref = zipfile.ZipFile("~/nbs/asgmnt1/test.zip", 'r')
        zip_ref.extractall(dir+dirList[0])
        zip_ref.close()
    elif (f.startswith("Train") or f.startswith("train")):
        zip_ref = zipfile.ZipFile("~/nbs/asgmnt1/train.zip", 'r')
        zip_ref.extractall(dir+dirList[8])
        zip_ref.close()

#move files to valid directory
files = os.listdir(dir+dirList[8])
for f in files:
    if (f.startswith("dog")):
        if dogValid > 0:
            shutil.move(dir+dirList[8]+f,dir+dirList[2])
            dogValid -= 1
    elif (f.startswith("cat")):
        if catValid > 0:
            shutil.move(dir+dirList[8]+f,dir+dirList[3])
            catValid -= 1

#copy files to sample valid dogs directory
files = os.listdir(dir+dirList[2])            
for f in files:
    if (f.startswith("dog")):
        if dogSampleValid > 0:
            shutil.copy(dir+dirList[2]+f,dir+dirList[12])
            dogSampleValid -= 1

#copy files to sample valid cats directory
files = os.listdir(dir+dirList[3])            
for f in files:          
    if (f.startswith("cat")):
        if catSampleValid > 0:
            shutil.copy(dir+dirList[3]+f,dir+dirList[13])
            catSampleValid -= 1
            
#move files to train directory
files = os.listdir(dir+dirList[8])            
for f in files:
    if (f.startswith("dog")):
        shutil.move(dir+dirList[8]+f,dir+dirList[9])
    elif (f.startswith("cat")):
        shutil.move(dir+dirList[8]+f,dir+dirList[10])

#copy files to sample train dogs directory
files = os.listdir(dir+dirList[9])            
for f in files:
    if (f.startswith("dog")):
        if dogSampleTrain > 0:
            shutil.copy(dir+dirList[9]+f,dir+dirList[6])
            dogSampleTrain -= 1
            
#copy files to sample train cats directory
files = os.listdir(dir+dirList[10])
for f in files:  
    if (f.startswith("cat")):
        if catSampleTrain > 0:
            shutil.copy(dir+dirList[10]+f,dir+dirList[7])
            catSampleTrain -= 1