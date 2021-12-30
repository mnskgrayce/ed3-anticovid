import Alert from "react-bootstrap/Alert";
import socketIOClient from "socket.io-client";

const ENTRANCE_PEOPLE = "Qr_data"

const WarningLogBar = ({ url }) => {
  const date = new Date();
  //List people 
  var queue = [];

  // Socket 
  const ENDPOINT = `${url}:4000`;
  const socket = socketIOClient(ENDPOINT);

  socket.on(ENTRANCE_PEOPLE, function (myData) {
    // push to queue name

    if(queue.length === 2){
      queue.shift();  //put 
    }
    queue.push(myData);

    console.log(queue[0])
    console.log(queue[1])
    console.log(queue.length)
    switch(queue.length){
      case 1:
        document.getElementById("name_id_1").innerHTML = queue[0] + " has entered the room"
        document.getElementById("name_id_2").innerHTML = "ID 2"
        break;
      case 2:
        document.getElementById("name_id_1").innerHTML = queue[0] + " has entered the room"
        document.getElementById("name_id_2").innerHTML = queue[1] + " has entered the room"
        break;
      default:
        break;   
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
        <div className="col-6 text-white"
          style={{
            textAlign:"center",
            margin:"auto"
          }}>
          <h4>{date.toString()}</h4>
        </div>
        <div className="col-6 " 
              style={{
                fontSize:"1.5rem",
              }}>
          {/* <h4 id="name1_id">Han has entered the room</h4>
          <h4 id="name2_id">Duc has entered the room</h4> */}
          <ul className="list-group">
            <li id="name_id_1" className="list-group-item disabled" 
              style={{
                fontColor:"blue",
              }}>ID 1</li>
            <li id="name_id_2" className="list-group-item"
              style={{
                fontColor:"blue",
              }}>ID 2</li>
          </ul>
      </div>
      
    </div>

      
    </div>
    
  );
};

export default WarningLogBar;
