import Card from "react-bootstrap/Card";
import ListGroup from "react-bootstrap/ListGroup";
import { FaTemperatureHigh } from "react-icons/fa";
import { FaWater } from "react-icons/fa";
import { GiWateringCan } from "react-icons/gi";

const SensorData = ({ temperature, humidity, moisture }) => {
  return (
    <Card>
      <ListGroup className="text-left text-uppercase text-sm" variant="flush">
        <ListGroup.Item>
          <FaTemperatureHigh
            style={{ display: "inline-block" }}
            className="mr-2"
          />
          Temperature:
          <span className="ml-2 font-bold">{temperature}</span> &deg;C
        </ListGroup.Item>

        <ListGroup.Item>
          <FaWater style={{ display: "inline-block" }} className="mr-2" />
          Humidity: <span className="ml-2 font-bold">{humidity}</span> &#37;
        </ListGroup.Item>

        <ListGroup.Item>
          <GiWateringCan style={{ display: "inline-block" }} className="mr-2" />
          Moisture: <span className="ml-2 font-bold">{moisture}</span> &#37;
        </ListGroup.Item>
      </ListGroup>
    </Card>
  );
};

export default SensorData;
