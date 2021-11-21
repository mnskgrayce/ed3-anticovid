import { useEffect, useRef, useState } from "react";

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
  const [temperature, setTemperature] = useState(0);
  const [humidity, setHumidity] = useState(0);
  const [totalPeople, setTotalPeople] = useState(0);

  // Live update sensor data
  useInterval(async () => {
    console.log("Polling sensor data...");

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

        console.log("Temperature: ", temperature, "\nHumidity: ", humidity);
      })
      .catch((error) => {
        console.log(error);
      });
  }, 4000);

  // Live update motion data
  useInterval(async () => {
    console.log("Polling motion data...");

    fetch("http://192.168.0.103:8000/motion/1")
      .then((response) => {
        if (response.ok) {
          return response.json();
        }
        throw response;
      })
      .then((data) => {
        setTotalPeople(data.total);

        console.log("Total people: ", totalPeople);
      })
      .catch((error) => {
        console.log(error);
      });
  }, 10000);

  return (
    <div>
      <h1>Home Page</h1>
      <p>Temperature: {temperature}</p>
      <p>Humidity: {humidity}</p>
      <p>Total People: {totalPeople}</p>
    </div>
  );
};

export default HomePage;
