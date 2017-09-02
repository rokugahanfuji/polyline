function initializeDatabase(list){
    for (var key of list){
        var replacedkey = key.replace(".txt","");
        if (typeof localStorage[replacedkey] !== "undefined")
            continue;
        var compressed = LZString.compressToUTF16(httpGet('./'+key))
        localStorage.setItem(replacedkey,compressed);
    }
    var box = {};
    for (var key in localStorage){
        box[key] = LZString.decompressFromUTF16(localStorage[key]);
    }

    setSelectBox(box);
};