import "./App.css";

import React from "react";
import { useEffect, useRef, useState } from "react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";

import WarningLogBar from "./components/WarningLogBar";
import SensorBar from "./components/SensorBar";
import VisionCameraPanel from "./components/VisionCameraPanel";
import QRCameraPanel from "./components/QRCameraPanel";
import MotionBar from "./components/MotionBar";


function App() {
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

  // Sensor variables
  const [temperature, setTemperature] = useState(35);
  const [humidity, setHumidity] = useState(50);
  const [moisture, setMoisture] = useState(70);
  // Motion variables
  const [entries, setEntries] = useState(0);
  const [exits, setExits] = useState(0);
  const [totalPeople, setTotalPeople] = useState(0);
  
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
        setMoisture(data.moisture);
      })
      .catch((error) => {
        console.log(error);
      });
  }, 500);

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
        setEntries(data.people_in);
        setExits(data.people_out);
        setTotalPeople(data.total_people);
      })
      .catch((error) => {
        console.log(error);
      });
  }, 1000);

  // Update UI when data changes
  useEffect(() => {
    console.log(
      "Temperature: ",
      temperature,
      "\nHumidity: ",
      humidity,
      "\nMoisture: ",
      moisture
    );
  }, [temperature, humidity, moisture]);

  useEffect(() => {
    console.log(
      "Entries: ",
      entries,
      "\nExits: ",
      exits,
      "\nTotal: ",
      totalPeople
    );
  }, [entries, exits, totalPeople]);

  return (
    <div className="App">
      <div className="d-flex flex-column vh-100 bg-transparent">
        <div>
          <WarningLogBar />
        </div>
        <div>
          <SensorBar
            temperature={temperature}
            humidity={humidity}
            moisture={moisture}
          />
        </div>
        <Container className="flex-grow-1 mb-2">
          <Row className="h-100">
            <Col xs={8}>
              <VisionCameraPanel />
            </Col>
            <Col xs={4}>
              <QRCameraPanel />
              <MotionBar
                entries={entries}
                exits={exits}
                totalPeople={totalPeople}
              />
            </Col>
          </Row>
        </Container>
        <div className="bg-body border-top">
          <p className="mb-0 ms-2 text-muted text-start">
            <small>
              ANTICOVID Team | RMIT University Vietnam |{" "}
              <a
                className="text-decoration-none link-primary"
                href="https://github.com/mnskgrayce/ed3-anticovid"
              >
                GitHub
              </a>
            </small>
          </p>
        </div>
      </div>
    </div>
  );
}

export default App;
