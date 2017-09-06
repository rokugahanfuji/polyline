var map, nowPolyline

function initialize() {
    var myLatlng = new google.maps.LatLng(36.103774791666666,140.08785504166664);
    var myOptions = genOptions(myLatlng);
    map = new google.maps.Map(document.getElementById("map"),myOptions);
    initializeFileComponents();
    if (localStorage.length != 0){
        setLocalStorageToSelectBox();
    }
};

function initializeFileComponents(){
    var inputFile = document.getElementById('file');
    var reader = new FileReader();

    function fileChange(ev) {
        var target = ev.target;
        var file = target.files[0];
        reader.readAsText(file);
    };

    function fileLoad() {
        clearSelectBox();
        initializeDatabase(reader.result);
        setLocalStorageToSelectBox();
        console.log("loaded.")
    };

    inputFile.addEventListener('change', fileChange, false);
    reader.addEventListener('loadend', fileLoad, false);
};

function setLocalStorageToSelectBox(){
    var box = {};
    for (var key in localStorage){
        box[key] = getPolylineFromLocalStorage(key);
    }
    setSelectBox(box);
}

function clearLocalStorage(){
    localStorage.clear();
    clearSelectBox();
    if (localStorage.length == 0){
        alert("Clear LocalStorage.")
    }
}

function httpGet(url){
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", url,false);
    xmlHttp.send(null);
    return xmlHttp.responseText;
};

function setSelectBox(selectBox){
    var select = document.getElementById('list');    
    for ( var i in selectBox ) {
        var option = document.createElement('option');
        option.setAttribute('value', selectBox[i]);
        option.innerHTML = i;
        select.appendChild(option);
    }
};

function clearSelectBox(){
    var select = document.getElementById("list");
    for(i = select.options.length - 1 ; i >= 0 ; i--)
    {
        select.remove(i);
    }
}

function setText(){
    var box = document.getElementById('encodedTextBox');
    box.innerHTML=document.getElementById('list').value;
    setPoint();
};

function setPoint(){
    var decodePath = google.maps.geometry.encoding.decodePath(document.getElementById('encodedTextBox').value);
    if (typeof nowPolyline !== "undefined"){
        nowPolyline.setMap(null);
    }
    nowPolyline = createPolyline(decodePath,map);
    map.setZoom(10);
    map.panTo(new google.maps.LatLng(decodePath[0].lat(),decodePath[0].lng()));
};

function genOptions(myLatlng){
    return {
        zoom: 8,
        center: myLatlng,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    }
};

function createPolyline(decodedPath,map){
    return new google.maps.Polyline({
        path: decodedPath,
        strokeColor: "#FF0000",
        strokeOpacity: 1.0,
        strokeWeight: 2,
        map: map
    });
};
