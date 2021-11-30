import socketIOClient from "socket.io-client";

const QRCameraPanel = () => {
  const ENDPOINT = "http://10.247.208.54:4000";

  const socket = socketIOClient(ENDPOINT);
  socket.on('video',function(data){
    var string_src = "data:image/png;base64, "+data;
    document.getElementById("myImageID").src=string_src;
  })

  socket.on('close',function(data){
    document.getElementById('myImageID').src="./logo192.png";
  })

  return (
    <div className="border shadow-sm bg-body p-2 rounded h-75">
      <p className="text-start text-uppercase text-muted">
        {/* <small>QR Camera</small> */}
        <img id="myImageID" src="" alt="QR Camera" width="400" height="500"></img>
      </p>
    </div>
  );
};

export default QRCameraPanel;
