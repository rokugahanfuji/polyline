var map, nowPolyline

function initialize() {
    var decodedPath = google.maps.geometry.encoding.decodePath('}~kvHmzrr@ba\\hnc@jiu@r{Zqx~@hjp@pwEhnc@zhu@zflAbxn@fhjBvqHroaAgcnAp}gAeahAtqGkngAinc@_h|@r{Zad\\y|_D}_y@swg@ysg@}llBpoZqa{@xrw@~eBaaX}{uAero@uqGadY}nr@`dYs_NquNgbjAf{l@|yh@bfc@}nr@z}q@i|i@zgz@r{ZhjFr}gApob@ff}@laIsen@dgYhdPvbIren@'); 
    var myLatlng = new google.maps.LatLng(decodedPath[0].lat(), decodedPath[0].lng());
    var myOptions = genOptions(myLatlng);
    map = new google.maps.Map(document.getElementById("map"), myOptions);
    nowPolyline = createPolyline(decodedPath,map);
    initializeJsonFile();
    if (localStorage.length != 0){
        setLocalStorageToSelectBox();
    }
};

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

function setText(){
    var box = document.getElementById('encodedTextBox');
    box.innerHTML=document.getElementById('list').value;
    setPoint();
};

function setPoint(){
    var decodePath = google.maps.geometry.encoding.decodePath(document.getElementById('encodedTextBox').value);
    nowPolyline.setMap(null);
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
