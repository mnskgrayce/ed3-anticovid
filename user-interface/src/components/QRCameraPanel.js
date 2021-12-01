import socketIOClient from "socket.io-client";

const QRCameraPanel = ({checkout}) => {
  const ENDPOINT = "http://10.247.195.173:4000";

  const socket = socketIOClient(ENDPOINT);
  socket.on('video',function(data){
    var string_src = "data:image/png;base64, "+data;
    document.getElementById("myImageID").src=string_src;
  })

  return (
    <div className="border shadow-sm bg-body p-2 rounded h-75">
      <h3>{checkout === 0
              ? "0"
              : checkout === 1
              ? "1"
              : checkout ===2
              ? "2"
              : checkout === 3
              ? "3"
              : ""}</h3>

      <img className="w-100 h-100 pb-5" id="myImageID" src="" alt="QR Camera"></img>
    </div>
   
);
};

export default QRCameraPanel;
