import socketIOClient from "socket.io-client";
import Badge from "react-bootstrap/Badge";

const QRCameraPanel = ({ url }) => {
  const ENDPOINT = `${url}:4000`;

  const socket = socketIOClient(ENDPOINT);
  socket.on("video", function (data) {
    var string_src = "data:image/png;base64, " + data;
    document.getElementById("myImageID").src = string_src;
  });

  socket.on("checkout", function (state_people) {
    var inner_checkout = "";
    var color = "red";
    switch (state_people) {
      case 1:
        inner_checkout = "QR is valid!";
        color = "green";
        break;
      case 2:
        color = "red";
        inner_checkout = "Room is full!";
        break;
      case 3:
        color = "red";
        inner_checkout = "QR is invalid!";
        break;
      case 4:
        color = "green";
        inner_checkout = "Exiting the room...";
        document.getElementById("myImageID").src = './exit.jpeg';

        break;
    }
    document.getElementById("checkout_id").innerHTML = inner_checkout;
    document.getElementById("checkout_id").style.backgroundColor = color;
  });

  socket.on("fps_qr", function (fqs_qr) {
    document.getElementById("fps_id").innerHTML = "FPS: " + fqs_qr;
  });

  return (
    <div className="border shadow-sm bg-body mt-5 p-2 rounded">
      <div className="position-relative">
        <Badge
          id="checkout_id"
          className="position-absolute top-0 start-0"
        ></Badge>
        <p
          id="fps_id"
          className="mb-0 text-end fs-6 font-monospace position-absolute top-0 end-0"
          style={{
            color: "red",
          }}
        >
          FPS:
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
