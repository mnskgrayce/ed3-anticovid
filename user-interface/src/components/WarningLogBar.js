import Alert from "react-bootstrap/Alert";
import socketIOClient from "socket.io-client";

const WarningLogBar = ({ url }) => {
  const date = new Date();
  const warningMessage = "Social distance violation detected!";

  // constant variable 
  const ALARM_SOCIAL_DISTANCE = "alarm_distance"
  const SAFE_SOCIAL_DISTANCE = "safe_distance"
  const ALARM_PEOPLE_GATHERING = "alarm_gathering"
  const SAFE_PEOPLE_GATHERING = "safe_gathering"

  // HEADER socket received 
  const SOCIAL_DISTANCE_SOCKET = "socialDistance"
  const PEOPLE_GATHERING_SOCKET = "peopleGathering"

  // Socket 
  const ENDPOINT = `${url}:5000`;
  const socket = socketIOClient(ENDPOINT);

  // Socket send social distance 
  socket.on(SOCIAL_DISTANCE_SOCKET, function (social_distance_data) {
    if(social_distance_data ===  ALARM_SOCIAL_DISTANCE){
      // Warning for social distance
      document.querySelector(".social_distance_alarm").style.filter = "brightness(100%)";
      document.querySelector(".social_distance_safe").style.filter = "brightness(50%)";
    }

    else if (social_distance_data ===  SAFE_SOCIAL_DISTANCE){
      // safe for social distance 
      document.querySelector(".social_distance_alarm").style.filter = "brightness(50%)";
      document.querySelector(".social_distance_safe").style.filter = "brightness(100%)";
    }
    // console.log(social_distance_data);
  });

  // Socket send social distance 
  socket.on(PEOPLE_GATHERING_SOCKET, function (people_gathering_data) {
    if(people_gathering_data ===  ALARM_PEOPLE_GATHERING){
      // Warning for people gathering
      document.querySelector(".people_gathering_alarm").style.filter = "brightness(100%)";
      document.querySelector(".people_gathering_safe").style.filter = "brightness(50%)";
    }

    else if (people_gathering_data ===  SAFE_PEOPLE_GATHERING){
      // safe for people gathering 
      document.querySelector(".people_gathering_alarm").style.filter = "brightness(50%)";
      document.querySelector(".people_gathering_safe").style.filter = "brightness(100%)";
    }
  });

  return (
    // <Alert variant="danger" className="text-start shadow-sm mt-2 mb-0 mx-4">
    //   <Alert.Heading className="fs-2 fw-bold">Warning Logs</Alert.Heading>

    //   <p className="mb-0 fs-4">
    //     {warningMessage}
    //     <small className="text-muted ms-2">{date.toString()}</small>
    //   </p>
      
    // </Alert>
    <div className="border shadow-sm p-2 rounded bg-dark m-2">
      <div className="row">
        <div className="col-2">
          {/* soical distance  alarm*/}
          <img
            className="social_distance_alarm"
            src="./UI_Vision/social_distance_alarm.jpg"
            alt="social distance alarm"
            style={{ objectFit: "cover", maxWidth: "10vw", maxHeight: "10vh" }}
          ></img>
        </div>
        <div className="col-2">
          {/* soical distance  safe*/}
          <img
            className="social_distance_safe"
            src="./UI_Vision/social_distance_safe.jpg"
            alt="social distance safe"
            style={{ objectFit: "cover", maxWidth: "10vw", maxHeight: "10vh" }}
          ></img>
        </div>

        <div className="col-2">
          {/* people gathering alarm */}
          <img
            className="people_gathering_alarm"
            src="./UI_Vision/people_gathering_alarm.png"
            alt="people gathering alarm"
            style={{ objectFit: "cover", maxWidth: "10vw", maxHeight: "10vh" }}
          ></img>
        </div>
        <div className="col-2">
          {/* people gathering safe*/}
          <img
            className="people_gathering_safe"
            src="./UI_Vision/people_gathering_safe.png"
            alt="people gathering safe"
            style={{ objectFit: "cover", maxWidth: "10vw", maxHeight: "10vh" }}
          ></img>
        </div>

        <div className="col-4 text-white">
          {date.toString()}
        </div>
      </div>
    </div>
    
  );
};

export default WarningLogBar;
