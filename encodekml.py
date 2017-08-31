"""This is a comvert program using polyline."""
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/lib')
import xml.etree.ElementTree as ET
import gistfile1 as GIST

txtdir = os.path.dirname(os.path.abspath(__file__)) + '/txt'
kmldir = os.path.dirname(os.path.abspath(__file__)) + '/kml'
if os.path.exists(txtdir) == False:
    os.mkdir(txtdir)

def getCoordinateFromKML(path):
    tree = ET.parse(path)
    root = tree.getroot()
    url = root.tag[:-3]
    return tree.find(".//"+url+"coordinates").text

def createEncodedPolylineString(colist):
    coodinates = []
    for element in colist:
        x, y = element.split(",")
        tup = (float(x),float(y))
        coodinates.append(tup)
        
    return GIST.encode_coords(coodinates)
for f in os.listdir(kmldir):
    path = kmldir+"/"+f
    coodinatelist = getCoordinateFromKML(path).split(" ")
    f = open(txtdir+"/"+f[:-3]+".txt","w")
    f.write(createEncodedPolylineString(coodinatelist).replace('\\','\\\\'))
    f.close()