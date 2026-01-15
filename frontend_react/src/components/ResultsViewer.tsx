import { useState, useEffect } from "react";
import axios from "axios";

function ResultsViewer() {
  const [items, setItems] = useState<Array<string>>([]);
  const [file, setFile] = useState<string>("");

  useEffect(() => {
    const fetchItems = async () => {
      // A placeholder URL - **Replace this with your actual API endpoint**
      const API_URL = "http://127.0.0.1:8080/mri/results";

      try {
        const response = await axios.get(API_URL);
        // Assuming the response data is an array of objects
        setItems(response.data.images);
      } catch (err) {
        console.error("Error fetching data:", err);
      }
    };

    fetchItems();
    //manually stat papayajs
    if (typeof papaya !== 'undefined') {
        papaya.Container.startPapaya();
    }
  }, []);
  const handleChange = async (event) => {
    const selectedValue = event.target.value;
    setFile(selectedValue);

    const value = await fetchStringValue(selectedValue);

    let finalVal = `data:image/nifti;base64,${value}`;
    let params = [];
    params["showControlBar"] = true;
    params["images"] =[finalVal];
    //console.log(params);
    //console.log("1,",window.papayaContainers)
    //console.log("2",papaya.Container.containers[0]);
    papaya.Container.resetViewer(0, params);
    //console.log(finalVal);
  };

  const fetchStringValue = async (id: string) => {
    // Replace this with your actual API endpoint and logic for the single value
    //const INITIAL_API_ENDPOINT = 'http://127.0.0.1:8080/mri/images'
    const API_ENDPOINT = `http://127.0.0.1:8080/mri/results/${id}`;
    console.log(`📡 Hitting endpoint: ${API_ENDPOINT}`);

    try {
      // Simulate network delay and data response
      const response = await axios.get(API_ENDPOINT);
      return response.data.basestr;
    } catch (error) {
      console.error(`Error fetching strValue for ${id}:`, error);
      return null;
    }
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
      <div className="row">
        <div className="col-8">
          <div className="papaya" data-params="params" id="ii"></div>
        </div>
      </div>
    </>
  );
}

export default ResultsViewer;
