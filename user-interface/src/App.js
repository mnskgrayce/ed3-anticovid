import "./App.css";
import React from "react";

import WarningLogBar from "./components/WarningLogBar";
import SensorBar from "./components/SensorBar";
import VisionCameraPanel from "./components/VisionCameraPanel";
import QRCameraPanel from "./components/QRCameraPanel";
import MotionBar from "./components/MotionBar";
import Footer from "./components/Footer";

function App({ url }) {
  return (
    <div className="App">
      <div className="container-fluid p-0 bg-transparent overflow-hidden">
        <WarningLogBar />
        <SensorBar url={url} />

        <div className="d-flex flex-row justify-content-evenly align-items-stretch px-2">
          <VisionCameraPanel url={url} />
          <div className="d-flex flex-column">
            <QRCameraPanel url={url} />
            <MotionBar url={url} />
          </div>
        </div>

        <Footer />
      </div>
    </div>
  );
}

export default App;
