import socketIOClient from "socket.io-client";

const SensorBar = ({ url }) => {
  const ENDPOINT = `${url}:4000`;

  const socket = socketIOClient(ENDPOINT);
  socket.on("sensor", function (data) {
    var temperature = data.temperature;
    var humidity = data.humidity;
    var moisture = data.moisture;

    //  Set value for the temperature
    document.getElementById("temp_id").innerHTML = temperature;
    document.getElementById("humidity_id").innerHTML = humidity;
    document.getElementById("moist_id").innerHTML = moisture;

    // Temperature setting for backgroundcolor and status
    if (temperature <= 20) {
      document.getElementById("badge_temp_id").style.backgroundColor = "blue";
      document.getElementById("badge_temp_id").innerHTML = "cold";
    } else if (temperature > 20 && temperature < 35) {
      document.getElementById("badge_temp_id").style.backgroundColor = "green";
      document.getElementById("badge_temp_id").innerHTML = "normal";
    } else if (temperature >= 35) {
      document.getElementById("badge_temp_id").style.backgroundColor = "red";
      document.getElementById("badge_temp_id").innerHTML = "hot";
    }

    // Humidity setting for backgroundcolor and status
    if (humidity <= 50) {
      document.getElementById("badge_humi_id").style.backgroundColor = "red";
      document.getElementById("badge_humi_id").innerHTML = "dry";
    } else if (humidity > 50 && humidity < 70) {
      document.getElementById("badge_humi_id").style.backgroundColor = "green";
      document.getElementById("badge_humi_id").innerHTML = "moist";
    } else if (humidity >= 70) {
      document.getElementById("badge_humi_id").style.backgroundColor = "blue";
      document.getElementById("badge_humi_id").innerHTML = "wet";
    }

    // Moisture setting for backgroundcolor and status
    if (moisture <= 50) {
      document.getElementById("badge_moist_id").style.backgroundColor = "red";
      document.getElementById("badge_moist_id").innerHTML = "dry";
    } else if (moisture > 50 && moisture < 70) {
      document.getElementById("badge_moist_id").style.backgroundColor = "green";
      document.getElementById("badge_moist_id").innerHTML = "moist";
    } else if (moisture >= 70) {
      document.getElementById("badge_moist_id").style.backgroundColor = "blue";
      document.getElementById("badge_moist_id").innerHTML = "wet";
    }
  });

  return (
    <div className="shadow-sm border p-2 mx-4 my-2 bg-body rounded">
      <div className="d-flex justify-content-center align-items-center">
        <div className="px-5 border-end fs-3">
          <i
            className="bi bi-thermometer-high text-danger"
            style={{ fontSize: "2rem" }}
          ></i>
          Temperature:
          <span id="temp_id" className="ms-2 fw-bold">
            25
          </span>
          &deg;C
          <span
            id="badge_temp_id"
            className="ms-2 badge"
            style={{ backgroundColor: "orange" }}
          >
            normal
          </span>
        </div>

        <div className="px-5 border-end fs-3">
          <i
            className="bi bi-water me-2 text-success"
            style={{ fontSize: "2rem" }}
          ></i>
          Humidity:
          <span id="humidity_id" className="ms-2 fw-bold">
            50
          </span>
          &#37;
          <span
            id="badge_humi_id"
            className="ms-2 badge"
            style={{ backgroundColor: "red" }}
          >
            dry
          </span>
        </div>

        <div className="px-5 border-end fs-3">
          <i
            className="bi bi-moisture me-2 text-info"
            style={{ fontSize: "2rem" }}
          ></i>
          Moisture:
          <span id="moist_id" className="ms-2 fw-bold">
            70
          </span>
          &#37;
          <span
            className="ms-2 badge"
            id="badge_moist_id"
            style={{ backgroundColor: "blue" }}
          >
            wet
          </span>
        </div>
      </div>
    </div>
  );
};

export default SensorBar;
