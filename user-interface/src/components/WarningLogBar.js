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
    }

    else if (social_distance_data ===  SAFE_SOCIAL_DISTANCE){
      // safe for social distance 
    }
  });

    // Socket send social distance 
  socket.on(SOCIAL_DISTANCE_SOCKET, function (social_distance_data) {
    if(social_distance_data ===  ALARM_SOCIAL_DISTANCE){
      // Warning for social distance

    }

    else if (social_distance_data ===  SAFE_SOCIAL_DISTANCE){
      // safe for social distance 

    }
  });

  // Socket send social distance 
  socket.on(PEOPLE_GATHERING_SOCKET, function (people_gathering_data) {
    if(people_gathering_data ===  ALARM_PEOPLE_GATHERING){
      // Warning for people gathering

    }

    else if (people_gathering_data ===  SAFE_PEOPLE_GATHERING){
      // safe for people gathering 

    }
  });

  return (
    <Alert variant="danger" className="text-start shadow-sm mt-2 mb-0 mx-4">
      <Alert.Heading className="fs-2 fw-bold">Warning Logs</Alert.Heading>

      <p className="mb-0 fs-4">
        {warningMessage}
        <small className="text-muted ms-2">{date.toString()}</small>
      </p>
    </Alert>
  );
};

export default WarningLogBar;
