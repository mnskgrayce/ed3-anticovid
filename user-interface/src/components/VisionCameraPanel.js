import socketIOClient from "socket.io-client";

const VisionCameraPanel = ({ url }) => {
  const ENDPOINT = `${url}:4000`;

  const socket = socketIOClient(ENDPOINT);
  socket.on("videoVision", function (data) {
    var string_src = "data:image/png;base64, " + data;
    document.getElementById("mySocialID").src = string_src;
  });

  return (
    <div className="border shadow-sm p-2 rounded bg-dark">
      <img
        className=""
        id="mySocialID"
        src="https://picsum.photos/960/720"
        alt="Main Camera"
        style={{ width: "auto", "max-height": "440px", objectFit: "cover" }}
      ></img>
    </div>
  );
};

export default VisionCameraPanel;
