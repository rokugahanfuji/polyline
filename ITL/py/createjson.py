"""This program create json from compressed text file"""
import os
import re
import collections as cl
import json
import codecs

rootdir = os.path.dirname(os.path.abspath(__file__)) + '/'
compressdir = os.path.dirname(os.path.abspath(__file__)) + '/compress/'

list1 = []
for filename in sorted(os.listdir(compressdir)):
    head, ext = os.path.splitext(filename)
    if ext == ".txt":
        try:
            with open(compressdir + filename, "r") as f:
                list1.append((re.search("[0-9]+", filename).group(), unicode(f.read(), 'utf-8')))
        except Exception, err:
            print Exception, err
            print "[CREATE JSON] : Failed to create json."
            exit()
list1.sort(cmp=lambda x, y: cmp(int(x[0]), int(y[0])))

ys = []
for tup in list1:
    data = cl.OrderedDict()
    data["id"] = int(tup[0])
    data["area"] = tup[1].encode('utf-8')
    ys.append(data)

with open(compressdir + "sub.json", "w+") as f:
    try:
        json.dump(ys, f, indent=4, ensure_ascii=False)
        f.seek(0)
        with open(rootdir + "result.json", "w") as c:
            c.write(codecs.BOM_UTF16_LE)
            c.write((unicode(f.read(), 'utf-8')).encode('utf-16-le'))
    except Exception, err:
        print Exception, err
        print "[CREATE JSON] : Failed to create json."
        exit()
os.remove(compressdir + "sub.json")
print "[CREATE JSON] : success to create json. target : {} files".format(len(list1))
