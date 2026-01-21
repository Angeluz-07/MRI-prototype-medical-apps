import { useState, useEffect } from "react";
import axios from "axios";
import NiftiViewerContainer from "./NiftiViewerContainer";

function SelectOperation() {
  const [items, setItems] = useState<Array<string>>([]);
  const [file, setFile] = useState<string>("");

  const [operations, setOperations] = useState<Array<string>>([]);
  const [operation, setOperation] = useState<string>("");

  const [feedbackMsg, setfeedbackMsg] = useState<string>(
    "waiting for selection",
  );

  const [operationDescription, setOperationDescription] = useState<string>("");
  useEffect(() => {
    const fetchItems = async () => {
      // A placeholder URL - **Replace this with your actual API endpoint**
      const API_URL = "http://127.0.0.1:8080/mri/images";

      try {
        const response = await axios.get(API_URL);
        // Assuming the response data is an array of objects
        setItems(response.data.images);
      } catch (err) {
        console.error("Error fetching data:", err);
      }
    };

    fetchItems();

    const fetchOperations = async () => {
      // A placeholder URL - **Replace this with your actual API endpoint**
      const API_URL = "http://127.0.0.1:8080/operations";

      try {
        const response = await axios.get(API_URL);
        // Assuming the response data is an array of objects
        setOperations(response.data.items);
      } catch (err) {
        console.error("Error fetching data:", err);
      }
    };

    fetchOperations();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append("fileName", file); // Append binary data to FormData
    formData.append("operation", "dummy");

    //console.log(Object.fromEntries(formData));

    const API_ENDPOINT = "http://127.0.0.1:8080/mri/segment-brain";
    try {
      setfeedbackMsg("processing");
      const response = await axios.post(API_ENDPOINT, formData, {
        // It's good practice to explicitly set the Content-Type header,
        // but Axios/browser often handle this automatically for FormData.
        headers: {
          "Content-Type": "application/json",
        },
        // You can also add an onUploadProgress callback here for a progress bar
      });
      // 3. Handle the successful (asynchronous) response
      //const fname = response.data.filename
      setfeedbackMsg("success");
    } catch (error) {
      console.error("Error saving data:", error);
      setfeedbackMsg("error");
    }
  };

  const handleChange = (event) => {
    setFile(event.target.value);
  };

  const handleChangeOperation = (event) => {
    setOperation(event.target.value);
    setOperationDescription(`Description : ${event.target.value}`);
  };

  return (
    <>
      <form method="post" onSubmit={handleSubmit}>
        <div className="row">
          <div className="col-4">
            <select
              id=""
              className="form-select"
              value={file}
              onChange={handleChange}
              required
            >
              <option value="" disabled>
                Select input image
              </option>

              {items.map((item) => (
                <option key={item}>{item}</option>
              ))}
            </select>
          </div>
        </div>

        <NiftiViewerContainer
          imgId={file}
          endpoint={"mri/images"}
          containerId={30}
        ></NiftiViewerContainer>

        <div className="row">
          <div className="col-4">
            <select
              id=""
              className="form-select"
              value={operation}
              onChange={handleChangeOperation}
              required
            >
              <option value="" disabled>
                Select Operation
              </option>

              {operations.map((item) => (
                <option key={item.id} value={item.description}>
                  {item.name}
                </option>
              ))}
            </select>
          </div>

          <div className="col-4">
            <button className="btn btn-success" type="submit">
              Run
            </button>
          </div>
        </div>
        <div className="row">
          <div className="card col-4 m-2">{operationDescription}</div>
        </div>
      </form>
    </>
  );
}

export default SelectOperation;
