import socketIOClient from "socket.io-client";

const VisionCameraPanel = () => {
  const ENDPOINT = "http://192.168.100.7:4000";

  const socket = socketIOClient(ENDPOINT);
  socket.on('videoVision',function(data){
    var string_src = "data:image/png;base64, "+data;
    document.getElementById("mySocialID").src=string_src;
  })

  return (
    <div className="border shadow-sm bg-body p-2 rounded h-100">
      <p className="text-start text-uppercase text-muted">
        <img className="w-100 h-100" id="mySocialID" src="" alt="QR Camera"></img>
      </p>
    </div>
  );
};

export default VisionCameraPanel;
