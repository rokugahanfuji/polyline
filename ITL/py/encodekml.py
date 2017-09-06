"""This is a comvert program using polyline."""
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/lib')
import xml.etree.ElementTree as ET
import gistfile1 as GIST

txtdir = os.path.dirname(os.path.abspath(__file__)) + '/polyline/'
kmldir = os.path.dirname(os.path.abspath(__file__)) + '/kml/'


def getCoordinateStringFromKML(path):
    tree = ET.parse(path)
    root = tree.getroot()
    url = root.tag[:-3]
    return tree.find(".//" + url + "coordinates").text


# colist => [(lon,lat),(lon,lat),(lon,lat)...]
def createEncodedPolylineString(colist):
    coodinates = []
    for element in colist:
        if element == '':
            continue
        if element.count(',') == 1:
            x, y = element.split(",")
        else:
            x, y, z = element.split(",")
        tup = (float(x), float(y))
        coodinates.append(tup)
    return GIST.encode_coords(coodinates)


if os.path.exists(txtdir) == False:
    os.mkdir(txtdir)

successcount = failedcount = 0
failedlist = []
for filename in os.listdir(kmldir):
    head, ext = os.path.splitext(filename)
    if ext == ".kml":
        path = kmldir + filename
        coodinatelist = getCoordinateStringFromKML(path).split(" ")
        try:
            with open(txtdir + head.replace('p', '') + ".txt", "w") as f:
                f.write(createEncodedPolylineString(coodinatelist))
                successcount += 1
        except Exception,err:
            failedcount += 1
            print Exception,err
print "[ENCODE KML] : total: {} files, success: {} files, failed: {} files".format(successcount + failedcount, successcount, failedcount)
if failedcount > 0:
    print "failed : {}".format(failedlist)