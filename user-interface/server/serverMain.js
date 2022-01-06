// HEADER socket received and send 
const VIDEO_VISION_SOCKET = "videoVision"
const FPS_MAIN_CAMERA_SOCKET = "fpsMain"
const SOCIAL_DISTANCE_SOCKET = "socialDistance"
const PEOPLE_GATHERING_SOCKET = "peopleGathering"


const express = require("express");
const http = require("http");
const socketIo = require("socket.io");

const port = process.env.PORT || 5000;

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

    // Vision camera image 
    socket.on(VIDEO_VISION_SOCKET, function(data){
      let base64data = Buffer.from(data,'base64').toString('ascii')
      io.sockets.emit(VIDEO_VISION_SOCKET,base64data);
    })

    // Frame per second of the camera 
    socket.on(FPS_MAIN_CAMERA_SOCKET,function(fps_data){
      io.sockets.emit(FPS_MAIN_CAMERA_SOCKET,fps_data);
    });
    
  });

server.listen(port, () => console.log(`Listening on port ${port}`));