function initializeDatabase(json){
    localStorage.clear();
    var jsonObj = JSON.parse(json);
    var length = 0;
    for (var obj of jsonObj){
        localStorage.setItem(obj["id"],obj["area"]);
        length += obj["area"].length;
    }
    console.log(length);
};

function getPolylineFromLocalStorage(key){
    return LZString.decompressFromUTF16(localStorage[key]);
}