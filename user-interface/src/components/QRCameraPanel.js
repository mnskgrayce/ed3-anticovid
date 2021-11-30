import socketIOClient from "socket.io-client";

const QRCameraPanel = () => {
  const ENDPOINT = "http://192.168.100.7:4000";

  const socket = socketIOClient(ENDPOINT);
  socket.on('video',function(data){
    var string_src = "data:image/png;base64, "+data;
    document.getElementById("myImageID").src=string_src;
  })

  return (
    <div className="border shadow-sm bg-body p-2 rounded h-75">
      <p className="text-start text-uppercase text-muted">
        <img className="w-100 h-100" id="myImageID" src="" alt="QR Camera"></img>
      </p>
    </div>
  );
};

export default QRCameraPanel;
