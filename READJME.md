# OptimizedPolyline
For efficiency using polyline. Compress polyline and use it.
# Introduction
This repository has two directories.
### py
This directory has python files to do regarding polyline. - unzipkmz.py - To unzip kmz file to kml - encodekml.py - To encode kml to Polyline - compresspolyline.py - To compress polyline using LZ-String algorithm. - 
createjson.py - To create json from polylien files. - lib (Directory) - libraries
### webapp
This directory has HTML sites to use compressed polyline. - index.html - css (Directory) - js (Directory)
  - lz-string.js
  - txtManager.js
  - webapp.js
# Unzip, Encode, Compress and Create result.json
Create json file which has encoded and comppressed polyline. **Notice: worked by Pyhton 2.7** **kmz filename is excepted -> 'p'+num+'.kmz' (ex) p123.kmz, p150.kmz...**
### 0. Install lzString
- The algolithm "lz-String" library is needed to install your env by pip. - Excute below command. ``` pip install LZString ```
### 1. Unzip kmz
- 1.1 Put kmz files to py/kmz/ - 1.2 Excute unzipkmz.py - 1.3 If success, you can see new directory : /py/kml ``` $ ls compresspolyline.py createjson.py encodekml.py kmz lib unzipkmz.py $ python unzipkmz.py [UNZIP 
KMZ] : total: 1500 files, success: 1500 files, failed: 0 files $ ls compresspolyline.py createjson.py encodekml.py kml kmz lib unzipkmz.py ```
### 2. Encode kml
- 2.1 Excute encodekml.py - 2.2 If success , you can see new directory : /py/polyline **NOTICE:kmz filename is except 'p'+num+'.kmz' (ex) p123.kmz, p150.kmz...** ``` $ python encodekml.py [ENCODE KML] : total: 1500 
files, success: 1500 files, failed: 0 files $ ls compresspolyline.py createjson.py encodekml.py kml kmz lib polyline unzipkmz.py ```
### 3. Compress polyline
- 3.1 Excute compresspolyline.py - 3.2 If success, you can see new directory : /py/compress ``` $ python compresspolyline.py [COMPRESS POLYLINE] : total: 1500 files, success: 1500 files, failed: 0 files $ ls 
compress compresspolyline.py createjson.py encodekml.py kml kmz lib polyline unzipkmz.py ```
### 4. Create json
- 4.1 Excute createjson.py - 4.2 If suscess, you can see new file : /py/result.json ``` $ python createjson.py [CREATE JSON] : success create json. target : 1500 files $ ls compress compresspolyline.py createjson.py 
encodekml.py kml kmz lib polyline result.json unzipkmz.py ```
### 5. Check json
- 5.1 Open result.json with editor. - 5.2 result.json's encoding is "UTF-16-LE".If you can't see correctly, please check open setting of editor. - 5.3 json is like below. ``` [
    {
        "id": 1,
        "area": "ᗢᱛ䂬เܨᾠ "
    },
    {
        "id": 2,
        "area": "Ꮱ㱏䂜ق槆犠 "
    }
] ``` If you want you use again, I reccomend to clear generated folder.
# Use and Show result.json
### Use
- Open index.html
  - Choose : Choose result.json
  - Clear : Clear localstorage
### APIs
- Core APIs are only two in dataManager.js
  - initializeDatabase(json)
    - json : json String. refer to webapp.js and File API.
    - return: void
    - This method conduct storing compressed data to LocalStorage from json.
  - getPolylineFromLocalStorage(key)
    - key : localStroage's key
    - return : Polyline String
    - This method return polyline from LocalStorage after decompressing.
