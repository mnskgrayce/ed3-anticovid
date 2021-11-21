import Card from "react-bootstrap/Card";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";

const AboutPanel = () => {
  return (
    <>
      <Card className="text-left text-xs" style={{ lineHeight: 0.5 }}>
        <Card.Body>
          <div className="font-bold text-sm mb-2">
            <span className="mr-4">ANTICOVID TEAM</span>
            <a href="https://github.com/mnskgrayce/ed3-anticovid">GitHub</a>
          </div>

          <Row>
            <Col>
              <p>Tran Phuoc Thien - s3741198</p>
              <p>Joseph Tsao - s3804777</p>
              <p className="mb-1">Ku Chen Jui - s3636640</p>
            </Col>
            <Col>
              <p>Trinh Ngoc Duc - s3754338</p>
              <p className="mb-1">Nguyen Phuong Uyen - s3751882</p>
            </Col>
            <Col>
              <p>Tran Mach So Han - s3750789</p>
              <p className="mb-1">Nguyen Minh Trang - s3751450</p>
            </Col>
          </Row>
        </Card.Body>
        <Card.Footer className="text-muted">
          RMIT University Vietnam
        </Card.Footer>
      </Card>
    </>
  );
};

export default AboutPanel;
