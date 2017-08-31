import os
import shutil
import zipfile

kmzdir = os.path.dirname(os.path.abspath(__file__)) + '/kmz'
kmldir = os.path.dirname(os.path.abspath(__file__)) + '/kml'
if os.path.exists(kmldir) == False:
    os.mkdir(kmldir)

for filename in os.listdir(kmzdir):
    kmzpath = kmzdir + '/' + filename
    kmlpath = kmldir + '/' + filename[:-3] + "zip"
    shutil.copyfile(kmzpath, kmlpath)

for filename in os.listdir(kmldir):
    path = kmldir + '/' + filename
    if zipfile.is_zipfile(path) == True:
        with zipfile.ZipFile(path, 'r') as inputFile:
            inputFile.extractall(kmldir)
    os.remove(path)
