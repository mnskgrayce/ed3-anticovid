import { useEffect, useRef, useState } from "react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import SensorData from "./SensorData";
import AboutPanel from "./AboutPanel";

import MotionData from "./MotionData";

// Custom hook to repeatedly run a function
const useInterval = (callback, delay) => {
  const savedCallback = useRef();
  // Remember the latest callback
  useEffect(() => {
    savedCallback.current = callback;
  }, [callback]);

  // Set up the interval
  useEffect(() => {
    function tick() {
      savedCallback.current();
    }
    if (delay !== null) {
      const id = setInterval(tick, delay);
      return () => {
        clearInterval(id);
      };
    }
  }, [callback, delay]);
};

const HomePage = () => {
  const [temperature, setTemperature] = useState();
  const [humidity, setHumidity] = useState();
  const [totalPeople, setTotalPeople] = useState();

  // Fetch sensor data
  useInterval(async () => {
    fetch("http://192.168.0.103:8000/temp_sensor/1")
      .then((response) => {
        if (response.ok) {
          return response.json();
        }
        throw response;
      })
      .then((data) => {
        setTemperature(data.temperature);
        setHumidity(data.humidity);
      })
      .catch((error) => {
        console.log(error);
      });
  }, 200);

  // Fetch motion data
  useInterval(async () => {
    fetch("http://192.168.0.103:8000/motion/1")
      .then((response) => {
        if (response.ok) {
          return response.json();
        }
        throw response;
      })
      .then((data) => {
        setTotalPeople(data.total);
      })
      .catch((error) => {
        console.log(error);
      });
  }, 500);

  // Update UI when data changes
  useEffect(() => {
    console.log("Temperature: ", temperature, "\nHumidity: ", humidity);
  }, [temperature, humidity]);

  useEffect(() => {
    console.log("Total people: ", totalPeople);
  }, [totalPeople]);

  return (
    <Container fluid className="py-2">
      <Row>
        <Col className="col-auto">
          <SensorData temperature={temperature} humidity={humidity} />
        </Col>

        <Col>
          <MotionData
            enters={0}
            exits={0}
            total={totalPeople}
            warningMessage="Warning! This is your last warning."
          />
        </Col>
      </Row>

      <Row className="my-2" style={{ height: "80vh" }}>
        <Col className="col-8" style={{ backgroundColor: "#7FFFD4" }}>
          Room Camera
        </Col>
        <Col className="col-4" style={{ backgroundColor: "#008B8B" }}>
          QR Camera
        </Col>
      </Row>

      <Row>
        <Col>
          <AboutPanel />
        </Col>
      </Row>
    </Container>
  );
};

export default HomePage;
