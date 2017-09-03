function initializeDatabase(list){
   // localStorage.clear()
    var size = 0;
    for (var key of list){
        var replacedkey = key.replace(".txt","");
        if (typeof localStorage[replacedkey] !== "undefined" || key == '')
            continue;
        var compressed = httpGet('./'+key)
        localStorage.setItem(replacedkey,compressed);
        size += compressed.length;
        console.log(key);
        console.log(size);
    }
    var box = {};
    for (var key in localStorage){
        box[key] = LZString.decompressFromBase64(localStorage[key]);
    }
    setSelectBox(box);
};