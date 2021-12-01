import socketIOClient from "socket.io-client";

const VisionCameraPanel = () => {
  const ENDPOINT = "http://192.168.0.102:4000";

  const socket = socketIOClient(ENDPOINT);
  socket.on('videoVision',function(data){
    var string_src = "data:image/png;base64, "+data;
    document.getElementById("mySocialID").src=string_src;
  })

  return (
    <div className="border shadow-sm bg-body p-2 rounded h-100">
      <img className="w-80 h-80" id="mySocialID"  src="" alt="Main Camera"></img>
    </div>
  );
};

export default VisionCameraPanel;
