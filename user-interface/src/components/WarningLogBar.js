import Alert from "react-bootstrap/Alert";

const WarningLogBar = () => {
  const date = new Date();
  const warningMessage = "Social distance violation detected!";

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
