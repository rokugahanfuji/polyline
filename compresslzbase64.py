"""This program comperss txt to LZString"""
"This program need below command"
"pip install LZString"
import os
import lzstring
import shutil
txtdir = os.path.dirname(os.path.abspath(__file__)) + '/txt/'
compressdir = os.path.dirname(os.path.abspath(__file__)) + '/compress/'


# create compress dir
if os.path.exists(compressdir) == False:
    os.mkdir(compressdir)


successcount = failedcount = 0
lz = lzstring.LZString()
for filename in os.listdir(txtdir):
    try:
        with open(txtdir+filename,"r") as f:
            head, ext = os.path.splitext(filename)
            if ext == ".txt":
                with open(compressdir+filename,'w') as c:
                    cotext = lz.compressToBase64(f.read())
                    c.write(cotext)
                    print "complete compress : " + filename
                successcount += 1
    except:
        print "failed compress : " + filename
        failedcount += 1
print "total: {} files, success: {} files, failed: {} files".format(successcount+failedcount, successcount, failedcount)