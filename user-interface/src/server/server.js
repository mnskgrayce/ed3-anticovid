var express = require('express');
var socket = require('socket.io');
// var Buffer = require('buffer','utf8');

// App setup
var app = express();
var server = app.listen(4000,'0.0.0.0', function(){
    console.log('listening for requests on port 4000,');
});

// Static files
app.use(express.static('../public'));

//socket setup 
var io = socket(server);

io.on('connection',function(socket){
    console.log("made socket connection");

    socket.on('chat',function(data){
        console.log(data);
        io.sockets.emit('chat',data);
    })

    socket.on('login', function(data){
        io.sockets.emit('login',data);
    })

    socket.on('video', function(data){
    
        let base64data = Buffer.from(data,'base64').toString('ascii')
        io.sockets.emit('video',base64data);
    })

    socket.on('close', function(data){
        io.sockets.emit('video',data);
    })
});
