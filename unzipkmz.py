"""This program unzip kmz to kml"""
import os
import shutil
import zipfile

kmzdir = os.path.dirname(os.path.abspath(__file__)) + '/kmz/'
kmldir = os.path.dirname(os.path.abspath(__file__)) + '/kml/'
if os.path.exists(kmldir) == False:
    os.mkdir(kmldir)

for filename in os.listdir(kmzdir):
    head, ext = os.path.splitext(filename)
    if ext == ".kmz":
        kmzpath = kmzdir + filename
        kmlpath = kmldir + head + ".zip"
        shutil.copyfile(kmzpath, kmlpath)

for filename in os.listdir(kmldir):
    head, ext = os.path.splitext(filename)
    if ext == ".zip":
        path = kmldir + filename
    try:
        with zipfile.ZipFile(path, 'r') as inputFile:
            inputFile.extractall(kmldir)
        os.remove(path)
        print "complete unzip : " + head + ".kmz"
    except:
        print "failed unzip : " + head + ".kmz"
        os.remove(path)
