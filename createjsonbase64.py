"""This program create json from compressed text file"""
import os
import re
import collections as cl
import json
compressdir = os.path.dirname(os.path.abspath(__file__)) + '/compress/'

list1 = []
try:
    for filename in sorted(os.listdir(compressdir)):
        head, ext = os.path.splitext(filename)
        if ext == ".txt":
            with open(compressdir+filename,"r") as f:
                list1.append((re.search("[0-9]+", filename).group(), f.read()))
    list1.sort(cmp = lambda x, y: cmp(int(x[0]), int(y[0])))

    ys = []
    cnt = 0
    for i in range(len(list1)):
        data = cl.OrderedDict()
        data["id"] = int(list1[i][0])
        data["area"] = list1[i][1]
        ys.append(data)
    with open(compressdir+"result.json","w") as f:
        json.dump(ys,f,indent=4)
    print "success create json. target : {} files".format(cnt)
except:
    print "error"