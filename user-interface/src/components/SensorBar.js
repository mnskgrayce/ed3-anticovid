import Badge from "react-bootstrap/Badge";
import socketIOClient from "socket.io-client";

const SensorBar = ({url}) => {
  const ENDPOINT = `${url}:4000`;

  const socket = socketIOClient(ENDPOINT);
  socket.on("sensor", function (data) {
    //Dictionary  {"temperature": temperature,"humidity":humidity, "moisture":moisture}
    var temperature = data.temperature
    var  humidity = data.humidity
    var moisture = data.moisture

    //Temperature and background
    var color_temp = temperature <= 20? "blue": temperature > 20 && temperature < 35? "orange": temperature >= 35? "red": "blue"
    var status_temp = temperature <= 20? "cold": temperature > 20 && temperature < 35? "normal": temperature >= 35? "hot": "cold"
    document.getElementById("temp_id").innerHTML = temperature;
    document.getElementById("badge_temp_id").style.backgroundColor = color_temp
    document.getElementById("badge_temp_id").innerHTML = status_temp

    //Humidityand background
    var color_humi = humidity <= 50? "red": humidity > 50 && humidity < 70? "green": humidity >= 70? "blue": "red"
    var status_humi = humidity <= 50? "red": humidity > 50 && humidity < 70? "green": humidity >= 70? "blue": "red"
    document.getElementById("humidity_id").innerHTML = humidity;
    document.getElementById("badge_humi_id").style.backgroundColor = color_humi
    document.getElementById("badge_humi_id").innerHTML = status_humi

    //Moisture background
    var color_moist = moisture <= 50? "red": moisture > 50 && moisture < 70? "green": moisture >= 70? "blue": "red"
    var status_moist= moisture <= 50? "red": moisture > 50 && moisture < 70? "green": moisture >= 70? "blue": "red"
    document.getElementById("moist_id").innerHTML = moisture;
    document.getElementById("badge_moist_id").style.backgroundColor = color_moist
    document.getElementById("badge_moist_id").innerHTML = status_moist
  });

  return (
    <div className="shadow-sm border p-2 mx-4 my-2 mb-5 bg-body rounded">
      <div className="d-flex justify-content-center align-items-center">
        <div className="px-5 border-end">
          <i
            className="bi bi-thermometer-high text-danger"
            style={{ "font-size": "2rem" }}
          ></i>
          Temperature:<span id="temp_id" className="ms-2 fw-bold fs-5" ></span>
          &deg;C
          <Badge 
            id="badge_temp_id"
            className="ms-2"
          >
          </Badge>
        </div>

        <div className="px-5 border-end">
          <i
            className="bi bi-water me-2 text-success"
            style={{ "font-size": "2rem" }}
          ></i>
          Humidity:<span id="humidity_id" className="ms-2 fw-bold fs-5"></span>
          &#37;
          <Badge
            id="badge_humi_id"
            className="ms-2"
          >
          </Badge>
        </div>
        <div className="px-5 border-end">
          <i
            className="bi bi-moisture me-2 text-info"
            style={{ "font-size": "2rem" }}
          ></i>
          Moisture:<span id="moist_id" className="ms-2 fw-bold fs-5"></span>
          &#37;
          <Badge
            className="ms-2"
            id="badge_moist_id"
          >
          </Badge>
        </div>
      </div>
    </div>
  );
};

export default SensorBar;
