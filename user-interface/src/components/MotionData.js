import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Alert from "react-bootstrap/Alert";
import Card from "react-bootstrap/Card";

import { ImEnter } from "react-icons/im";
import { ImExit } from "react-icons/im";
import { BsFillPeopleFill } from "react-icons/bs";

const MotionData = ({ enters, exits, totalPeople, warningMessage }) => {
  return (
    <>
      <Alert variant="danger" className="mb-1">
        <Alert.Heading>{warningMessage}</Alert.Heading>
      </Alert>

      <Card className="p-1">
        <Row className="text-uppercase font-bold">
          <Col>
            <ImEnter style={{ display: "inline-block" }} className="mr-2" />
            Enters:
            <span className="ml-2 text-lg text-warning">{enters}</span>
          </Col>
          <Col>
            <ImExit style={{ display: "inline-block" }} className="mr-2" />
            Exits:
            <span className="ml-2 text-lg text-success">{exits}</span>
          </Col>
          <Col>
            <BsFillPeopleFill
              style={{ display: "inline-block" }}
              className="mr-2"
            />
            Total:
            <span className="ml-2 text-lg text-info">{totalPeople}</span>
          </Col>
        </Row>
      </Card>
    </>
  );
};

export default MotionData;
