import socketIOClient from "socket.io-client";

// HEADER socket received
const VIDEO_VISION = "videoVision"
const FPS_MAIN_CAMERA = "fpsMain"

const VisionCameraPanel = ({ url }) => {
  const ENDPOINT = `${url}:5000`;

  const socket = socketIOClient(ENDPOINT);
  socket.on(VIDEO_VISION, function (data) {
    var string_src = "data:image/png;base64, " + data;
    document.getElementById("mySocialID").src = string_src;
  });

  socket.on(FPS_MAIN_CAMERA, function (data) {
    document.getElementById("fps_main_id").innerHTML = "FPS: " + data;
  });

  return (
    <div>
      <div className="p-4 rounded bg-dark m-2 shadow-sm border">
        <div className="position-relative">
          <p
            className="mb-0 me-2 fw-bold text-end font-monospace position-absolute top-0 end-0"
            style={{
              fontSize:"1.5rem",
              color: "cyan",
            }}
            id="fps_main_id"
          >
            FPS: 0
          </p>
          <img 
            className=""
            id="mySocialID"
            src="https://picsum.photos/2400/1400"
            alt="Main Camera"
            style={{ objectFit: "cover", maxWidth: "70vw", maxHeight: "70vh", width:"1080px", height:"940px"}}
          ></img>
        </div>
      </div>

    </div>
  );
};

export default VisionCameraPanel;
