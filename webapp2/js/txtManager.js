function initializeDatabase(json){
    localStorage.clear()
    var jsonObj = JSON.parse(json)
    var length = 0;
    for (var obj of jsonObj){
        localStorage.setItem(obj["id"],obj["area"]);
        length += obj["area"].length;
    }
    var box = {};
    for (var key in localStorage){
        box[key] = LZString.decompressFromUTF16(localStorage[key]);
    }
    setSelectBox(box);
};


function initializeJsonFile(){

    var inputFile = document.getElementById('file');
    var reader = new FileReader();

    function fileChange(ev) {
        var target = ev.target;
        var file = target.files[0];
        var files = target.files;
        console.log(files);
        reader.readAsText(file);
    };

    function fileLoad() {
        console.log(reader.result);
    };

    inputFile.addEventListener('change', fileChange, false);
    reader.addEventListener('load', fileLoad, false);

};