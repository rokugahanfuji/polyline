"""This program create json from compressed text file"""
import os
import re
import collections as cl
import json
import codecs

compressdir = os.path.dirname(os.path.abspath(__file__)) + '/compress/'

list1 = []
try:
    for filename in sorted(os.listdir(compressdir)):
        head, ext = os.path.splitext(filename)
        if ext == ".txt":
            with open(compressdir+filename,"rb") as f:
                list1.append((re.search("[0-9]+", filename).group(), unicode(f.read(),'utf-8')))
    list1.sort(cmp = lambda x, y: cmp(int(x[0]), int(y[0])))
    ys = []
    cnt = 0
    for i in range(len(list1)):
        data = cl.OrderedDict()
        data["id"] = int(list1[i][0])
        data["area"] = list1[i][1].encode('utf-8')
        ys.append(data)
        cnt += 1
    with open(compressdir+"sub.json","wrb") as f:
        json.dump(ys,f,indent=4,ensure_ascii=False)

    with open(compressdir+"sub.json","rb") as f:
        with open(compressdir+"result.json","wb") as c:
            c.write(codecs.BOM_UTF16_LE)
            c.write((unicode(f.read(),'utf-8')).encode('utf-16-le'))
    os.remove(compressdir+"sub.json")
    print "success create json. target : {} files".format(cnt)
except Exception,err:
    print "error"
    print Exception,err