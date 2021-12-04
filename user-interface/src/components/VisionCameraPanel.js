import socketIOClient from "socket.io-client";

const VisionCameraPanel = ({ url }) => {
  const ENDPOINT = `${url}:5000`;

  const socket = socketIOClient(ENDPOINT);
  socket.on("videoVision", function (data) {
    var string_src = "data:image/png;base64, " + data;
    document.getElementById("mySocialID").src = string_src;
  });

  socket.on("fpsMain", function (data) {
    document.getElementById("fps_main_id").innerHTML = "FPS: "+data;
  });

  return (
    <div className="border shadow-sm  mt-5 p-2 rounded bg-dark">
      
      <div className="position-relative">
        <p
          className="mb-0 text-end fs-6 font-monospace position-absolute top-0 end-0"
          style={{
            color: "red",
          }}
          id="fps_main_id"
        >
          FPS: 
        </p>
        <img
          className=""
          id="mySocialID"
          src="https://picsum.photos/960/720"
          alt="Main Camera"
          style={{ width: "auto", "max-height": "440px", objectFit: "cover" }}
        ></img>
      </div>
    
    </div>
  );
};

export default VisionCameraPanel;
