import Table from "react-bootstrap/Table";

const MotionBar = ({ entries, exits, totalPeople }) => {
  return (
    <div className="border shadow-sm bg-body p-2 rounded h-25">
      <Table striped borderless hover className="h-100">
        <thead>
          <tr>
            <th className="text-success">
              <i
                className="bi bi-door-open-fill"
                style={{ "font-size": "1rem" }}
              ></i>
              Entries
            </th>
            <th className="text-danger">
              <i
                className="bi bi-door-closed-fill"
                style={{ "font-size": "1rem" }}
              ></i>
              Exits
            </th>
            <th className="text-info">
              <i
                className="bi bi-house-door-fill"
                style={{ "font-size": "1rem" }}
              ></i>
              Total
            </th>
          </tr>
        </thead>
        <tbody className="fs-3 fw-bold">
          <tr>
            <td className="text-success">{entries}</td>
            <td className="text-danger">{exits}</td>
            <td className="text-info">{totalPeople}</td>
          </tr>
        </tbody>
      </Table>
    </div>
  );
};

export default MotionBar;
