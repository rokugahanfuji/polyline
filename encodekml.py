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
        x, y = element.split(",")
        tup = (float(x), float(y))
        coodinates.append(tup)
    return GIST.encode_coords(coodinates)

# create txt dir
if os.path.exists(txtdir) == False:
    os.mkdir(txtdir)

# generate txt files
for filename in os.listdir(kmldir):
    head, ext = os.path.splitext(filename)
    if ext == ".kml":
        path = kmldir + filename
        coodinatelist = getCoordinateStringFromKML(path).split(" ")
        with open(txtdir + head + ".txt", "w") as f:
            try:
                f.write(createEncodedPolylineString(coodinatelist))
                f.close()
                print "complete generate txt : " + filename
            except:
                print "failed generate txt : " + filename
