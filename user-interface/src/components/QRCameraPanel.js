import socketIOClient from "socket.io-client";
import Badge from "react-bootstrap/Badge";

const QRCameraPanel = ({ url }) => {
  const ENDPOINT = `${url}:4000`;
  var glob_checkout = 0; 

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
        document.getElementById("myImageID").src = "./exit.jpeg";
        break;
      case 5:
        color = "red";
        inner_checkout = "No Scan";
        break;
      default:
        inner_checkout = "Waiting for data...";
        color = "blue";
    }
    document.getElementById("checkout_id").innerHTML = inner_checkout;
    document.getElementById("checkout_id").style.backgroundColor = color;
  });

  socket.on("fps_qr", function (fqs_qr) {
    document.getElementById("fps_id").innerHTML = "FPS: " + fqs_qr;
  });

  return (
    <div className="border shadow-sm p-4 rounded bg-dark m-2">
      <div className="position-relative">
        <span id="checkout_id" className="position-absolute top-0 start-0 badge" style={{ "font-size": "1.25rem" }}>
          Waiting for data...
        </span>
        <p
          id="fps_id"
          className="mb-0 me-2 fw-bold text-end font-monospace position-absolute top-0 end-0"
          style={{
            fontSize: "1.5rem",
            color: "cyan",
          }}
        >
          FPS: 0
        </p>

        <img
          className=""
          id="myImageID"
          src="https://picsum.photos/1200/900"
          alt="QR Camera"
          style={{ objectFit: "cover", maxWidth: "36vw", maxHeight: "50vh" }}
        ></img>
      </div>
    </div>
  );
};

export default QRCameraPanel;
