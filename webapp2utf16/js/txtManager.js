function initializeDatabase(json){
    localStorage.clear();
    var jsonObj = JSON.parse(json);
    var length = 0;
    for (var obj of jsonObj){
        localStorage.setItem(obj["id"],obj["area"]);
        length += obj["area"].length;
    }
    console.log(length);
    setLocalStorageToSelectBox();
};

function initializeJsonFile(){
    var inputFile = document.getElementById('file');
    var reader = new FileReader();

    function fileChange(ev) {
        var target = ev.target;
        var file = target.files[0];
        reader.readAsText(file);
    };

    function fileLoad() {
        initializeDatabase(reader.result);
        console.log("loaded.")
    };

    inputFile.addEventListener('change', fileChange, false);
    reader.addEventListener('loadend', fileLoad, false);

};

function setLocalStorageToSelectBox(){
    var box = {};
    for (var key in localStorage){
        box[key] = LZString.decompressFromUTF16(localStorage[key]);
    }
    setSelectBox(box);
}