import socketIOClient from "socket.io-client";
import Badge from "react-bootstrap/Badge";

const QRCameraPanel = ({checkout,fps}) => {
  const ENDPOINT = "http://192.168.0.102:4000";

  const socket = socketIOClient(ENDPOINT);
  socket.on('video',function(data){
    var string_src = "data:image/png;base64, "+data;
    document.getElementById("myImageID").src=string_src;
  })

  return (
    <div className="border shadow-sm bg-body p-2 rounded h-75">

      <Badge
            bg={`${
              checkout === "2"
                ? "warning"
                :checkout === "3"
                ? "warning"
                :checkout === "4"
                ? "success"
                : checkout === "1"
                ? "success"
                : ""
            }`}
            className="ms-2"
          >
            {checkout === "1"
              ? "QR Scan valid"
              : checkout === "2"
              ? "Room full"
              : checkout === "3"
              ? "QR Scan Invalid"
              : checkout === "4"
              ? "Exiting the room"
              : ""}
        </Badge>
      <p>FPS: {fps}</p>
      <img className="w-100 h-100 pb-5" id="myImageID" src="" alt="QR Camera"></img>
    </div>
   
);
};

export default QRCameraPanel;
