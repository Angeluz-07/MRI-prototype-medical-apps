import { useState, useEffect } from "react";
import axios from "axios";
import NiftiViewerContainer from "./NiftiViewerContainer";

function InputsViewer() {
  const [items, setItems] = useState<Array<string>>([]);
  const [file, setFile] = useState<string>("");

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

  const handleChange = async (event) => {
    const selectedValue = event.target.value;
    setFile(selectedValue);
  };

  return (
    <>
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
      <NiftiViewerContainer imgId={file} endpoint={"mri/images"}></NiftiViewerContainer>
      
    </>
  );
}

export default InputsViewer;
