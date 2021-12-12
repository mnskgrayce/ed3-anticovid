import Table from "react-bootstrap/Table";
import socketIOClient from "socket.io-client";

const MotionBar = ({ url }) => {
  const ENDPOINT = `${url}:4000`;

  const socket = socketIOClient(ENDPOINT);

  socket.on("motion", function (data) {
    //Dictionary  {"entries": entries,"exits":exits, "totalPeople":totalPeople}
    var entries = data.people_in;
    var exits = data.people_out;
    var totalPeople = data.total_people;

    //entries and background
    document.getElementById("entries_id").innerHTML = entries;

    //exits background
    document.getElementById("exits_id").innerHTML = exits;

    //totalPeople background
    document.getElementById("totalPeople_id").innerHTML = totalPeople;
  });

  return (
    <div className="border shadow-sm bg-body p-2 rounded">
      <Table striped borderless hover className="h-100">
        <thead>
          <tr>
            <th className=" fs-3 text-success">
              <i
                className="bi bi-door-open-fill"
                style={{ "font-size": "1.5rem" }}
              ></i>
              Entries
            </th>
            <th className="fs-3 text-danger">
              <i
                className="bi bi-door-closed-fill"
                style={{ "font-size": "1.5rem" }}
              ></i>
              Exits
            </th>
            <th className="fs-3 text-info">
              <i
                className="bi bi-house-door-fill"
                style={{ "font-size": "1.5rem" }}
              ></i>
              Total
            </th>
          </tr>
        </thead>
        <tbody className="fs-2 fw-bold" >
          <tr>
            <td id="entries_id" className="text-success">
              0
            </td>
            <td id="exits_id" className="text-danger">
              0
            </td>
            <td id="totalPeople_id" className="text-info">
              0
            </td>
          </tr>
        </tbody>
      </Table>
    </div>
  );
};

export default MotionBar;
