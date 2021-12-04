import Badge from "react-bootstrap/Badge";

const SensorBar = ({ temperature, humidity, moisture }) => {
  return (
    <div className="shadow-sm border p-2 mx-4 my-2 mb-5 bg-body rounded">
      <div className="d-flex justify-content-center align-items-center">
        <div className="px-5 border-end">
          <i
            className="bi bi-thermometer-high text-danger"
            style={{ "font-size": "2rem" }}
          ></i>
          Temperature:<span className="ms-2 fw-bold fs-5">{temperature}</span>
          &deg;C
          <Badge
            pill
            bg={`${
              temperature <= 20
                ? "info"
                : temperature > 20 && temperature < 35
                ? "warning"
                : temperature >= 35
                ? "danger"
                : ""
            }`}
            className="ms-2"
          >
            {temperature <= 20
              ? "cold"
              : temperature > 20 && temperature < 35
              ? "normal"
              : temperature >= 35
              ? "hot"
              : ""}
          </Badge>
        </div>

        <div className="px-5 border-end">
          <i
            className="bi bi-water me-2 text-success"
            style={{ "font-size": "2rem" }}
          ></i>
          Humidity:<span className="ms-2 fw-bold fs-5">{humidity}</span>
          &#37;
          <Badge
            pill
            bg={`${
              humidity <= 50
                ? "warning"
                : humidity > 50 && humidity < 70
                ? "success"
                : humidity >= 70
                ? "info"
                : ""
            }`}
            className="ms-2"
          >
            {humidity <= 50
              ? "dry"
              : humidity > 50 && humidity < 70
              ? "moist"
              : humidity >= 70
              ? "wet"
              : ""}
          </Badge>
        </div>
        <div className="px-5 border-end">
          <i
            className="bi bi-moisture me-2 text-info"
            style={{ "font-size": "2rem" }}
          ></i>
          Moisture:<span className="ms-2 fw-bold fs-5">{moisture}</span>
          &#37;
          <Badge
            pill
            bg={`${
              moisture <= 50
                ? "warning"
                : moisture > 50 && moisture < 70
                ? "success"
                : moisture >= 70
                ? "info"
                : ""
            }`}
            className="ms-2"
          >
            {moisture <= 50
              ? "dry"
              : moisture > 50 && moisture < 70
              ? "moist"
              : moisture >= 70
              ? "wet"
              : ""}
          </Badge>
        </div>
      </div>
    </div>
  );
};

export default SensorBar;
