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

successcount = failedcount = 0
failedList = []
for filename in os.listdir(kmldir):
    head, ext = os.path.splitext(filename)
    if ext == ".zip":
        path = kmldir + filename
        try:
            with zipfile.ZipFile(path, 'r') as inputFile:
                inputFile.extractall(kmldir)
                genfile = inputFile.extract(inputFile.infolist()[0], kmldir)
                os.rename(genfile, kmldir + head + ".kml")
            os.remove(path)
            successcount += 1
        except Exception, err:
            failedcount += 1
            failedList.append(filename)
            print Exception, err
print "[UNZIP KMZ] : total: {} files, success: {} files, failed: {} files".format(successcount + failedcount, successcount, failedcount)
if failedcount > 0:
    print "failed : {}".format(failedList)
