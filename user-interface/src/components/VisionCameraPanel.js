import socketIOClient from "socket.io-client";

const VisionCameraPanel = ({ url }) => {
  const ENDPOINT = `${url}:5000`;

  const socket = socketIOClient(ENDPOINT);
  socket.on("videoVision", function (data) {
    var string_src = "data:image/png;base64, " + data;
    console.log(string_src);
    document.getElementById("mySocialID").src = string_src;
  });

  socket.on("fpsMain", function (data) {
    document.getElementById("fps_main_id").innerHTML = "FPS: " + data;
  });

  return (
    <div className="border shadow-sm p-2 rounded bg-dark m-2">
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
          src="https://picsum.photos/2400/1400"
          alt="Main Camera"
          style={{ objectFit: "cover", maxWidth: "56vw", maxHeight: "70vh" }}
        ></img>
      </div>
    </div>
  );
};

export default VisionCameraPanel;
