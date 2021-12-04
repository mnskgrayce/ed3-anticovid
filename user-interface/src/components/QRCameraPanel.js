import socketIOClient from "socket.io-client";
import Badge from "react-bootstrap/Badge";

const QRCameraPanel = ({ checkout, fps, url }) => {
  const ENDPOINT = `${url}:4000`;

  const socket = socketIOClient(ENDPOINT);
  socket.on("video", function (data) {
    var string_src = "data:image/png;base64, " + data;
    document.getElementById("myImageID").src = string_src;
  });

  return (
    <div className="border shadow-sm bg-body mt-5 p-2 rounded">
      <div className="position-relative">
        <Badge
          className="position-absolute top-0 start-0"
          bg={`${
            checkout === "2"
              ? "warning"
              : checkout === "3"
              ? "warning"
              : checkout === "4"
              ? "success"
              : checkout === "1"
              ? "success"
              : ""
          }`}
        >
          {checkout === "1"
            ? "QR is valid!"
            : checkout === "2"
            ? "Room is full!"
            : checkout === "3"
            ? "QR is invalid!"
            : checkout === "4"
            ? "Exiting the room..."
            : ""}
        </Badge>
        <p
          className="mb-0 text-end fs-6 font-monospace position-absolute top-0 end-0"
          style={{
            color: "red",
          }}
        >
          FPS: {fps}
        </p>
        <img
          className=""
          id="myImageID"
          src="https://picsum.photos/640/480"
          alt="QR Camera"
          style={{ width: "auto", "max-height": "300px", objectFit: "cover" }}
        ></img>
      </div>
    </div>
  );
};

export default QRCameraPanel;
