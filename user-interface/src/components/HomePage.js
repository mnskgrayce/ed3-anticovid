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

  useInterval(async () => {
    console.log("Polling sensor data...");

    fetch("data/db.json")
      .then((response) => {
        if (response.ok) {
          return response.json();
        }
        throw response;
      })
      .then((data) => {
        setTemperature(data.temp_sensor[0].temperature);
        setHumidity(data.temp_sensor[0].humidity);
        setTotalPeople(data.motion[0].total);

        console.log(temperature, humidity, totalPeople);
      })
      .catch((error) => {
        console.log(error);
      });
  }, 5000);

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
