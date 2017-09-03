const http = require('http');
const fs = require('fs'); 

const server = http.createServer();
server.on('request', getJs);
server.listen(8888);
console.log('Server running ...');

const pattern = new RegExp(/\d+\.txt/);
function getJs(req, res) {
    let url = req.url;
    console.log(url);
    if ('/' == url) {
        fs.readFile('./index.html', 'UTF-8', function (err, data) {
            res.writeHead(200, {'Content-Type': 'text/html'});
            res.write(data);
            res.end();
        });
    } else if ('/js/webapp.js' == url) {
        fs.readFile('./js/webapp.js', 'UTF-8', function (err, data) {
            res.writeHead(200, {'Content-Type': 'text/javascript'});
            res.write(data);
            res.end();
        });
    } else if ('/js/txtManager.js' == url) {
        fs.readFile('./js/txtManager.js', 'UTF-8', function (err, data) {
            res.writeHead(200, {'Content-Type': 'text/javascript'});
            res.write(data);
            res.end();
        });
    } else if ('/js/lz-string.js' == url) {
        fs.readFile('./js/lz-string.js', 'UTF-8', function (err, data) {
            res.writeHead(200, {'Content-Type': 'text/javascript'});
            res.write(data);
            res.end();
        });
    } else if ('/css/webapp.css' == url) {
        fs.readFile('./css/webapp.css', 'UTF-8', function (err, data) {
            res.writeHead(200, {'Content-Type': 'text/css'});
            res.write(data);
            res.end();
        });
    } else if ('/gettextlist' == url){
        dir = '../compress/';
        fs.readdir(dir, function (err, files) {
            if (err) {
                throw err;
            }
            for(var txt of files){
                if (txt.split('.')[1] == "txt"){
                    res.write(txt.toString());
                    res.write(',');
                }
            }
            res.end();
          });
    } else if (pattern.test(url)){
        var name = url.match(pattern);
        fs.readFile('../compress/'+name[0], 'UTF-8', function (err, text) {
            res.writeHead(200, {'Content-Type': 'text/text'});
            res.end(text);
        });
    } else {
        res.writeHead(404);
        res.end("Error");
    }
}