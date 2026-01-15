import { useState, useEffect } from "react";
import axios from "axios";
|
function SelectOperation() {
  const [items, setItems] = useState<Array<string>>([]);
  const [file, setFile] = useState<string>();
  const [feedbackMsg, setfeedbackMsg] = useState<string>(
    "waiting for selection"
  );

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

  return (
    <>
      <form className="row" method="post" onSubmit={handleSubmit}>
        <div className="col-4">
          <select
            id="option"
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

        <div className="col-4">
          <select id="option" className="form-select" required>
            <option value="" disabled>
              Select operation
            </option>
            <option value="fast">Brain Masking</option>
          </select>
        </div>

        <div className="col-4">
          <button className="btn btn-success" type="submit">
            Run
          </button>
        </div>
        <p>{feedbackMsg}</p>
      </form>
    </>
  );
}

export default SelectOperation;
