const express = require("express");
const http = require("http");
const socketIo = require("socket.io");

const port = process.env.PORT || 4000;
// const index = require("../components");

const app = express();
app.use(express.static('../public'));

const server = http.createServer(app);

const io = socketIo(server, {
    cors: {
      origin: "*",
      methods: ["GET", "POST"]
    }
  });

io.on("connection", (socket) => {
    console.log("New client connected");

    socket.on("disconnect", () => {
      console.log("Client disconnected");
    });

    socket.on('video', function(data){
    
        let base64data = Buffer.from(data,'base64').toString('ascii')
        io.sockets.emit('video',base64data);
    })

    socket.on('videoVision', function(data){
      let base64data = Buffer.from(data,'base64').toString('ascii')
      io.sockets.emit('videoVision',base64data);
    })

    socket.on('sensor',function(sensor_data){
      io.sockets.emit('sensor',sensor_data);
    });

    socket.on('motion',function(sensor_data){
      io.sockets.emit('motion',sensor_data);
    });

    socket.on('checkout',function(sensor_data){
      io.sockets.emit('checkout',sensor_data);
    });

    socket.on('fps_qr', function(fps_qr){
      io.sockets.emit('fps_qr',fps_qr);
    })

    socket.on('Qr_data', function(myData){
      io.sockets.emit('Qr_data',myData);
    })   
  });

server.listen(port, () => console.log(`Listening on port ${port}`));