"""This is a comvert program using polyline."""
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/lib')
import xml.etree.ElementTree as ET
import gistfile1 as GIST

txtdir = os.path.dirname(os.path.abspath(__file__)) + '/txt/'
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
            x,y = element.split(",")
        else:
            x, y, z = element.split(",")
        tup = (float(x), float(y))
        coodinates.append(tup)
    return GIST.encode_coords(coodinates)

# create txt dir
if os.path.exists(txtdir) == False:
    os.mkdir(txtdir)

# generate txt files
successcount = failedcount = 0
for filename in os.listdir(kmldir):
    head, ext = os.path.splitext(filename)
    if ext == ".kml":
        path = kmldir + filename
        coodinatelist = getCoordinateStringFromKML(path).split(" ")
        try:
            with open(txtdir + head.replace('p','') + ".txt", "w") as f:
                #f.write(createEncodedPolylineString(coodinatelist).replace('\\','\\\\')
                f.write(createEncodedPolylineString(coodinatelist))
                print "complete generate txt : " + filename
                successcount += 1
        except:
            print "failed generate txt : " + filename
            failedcount += 1
print "total: {} files, successcount: {} files, failedcount: {} files".format(successcount+failedcount, successcount, failedcount)
