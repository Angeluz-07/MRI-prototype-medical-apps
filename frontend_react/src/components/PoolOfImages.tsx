import { useState, useEffect } from "react";
import axios from "axios";

function PoolOfImages() {
  const [file, setFile] = useState(null);
  const [items, setItems] = useState(["3"]);
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
    // The empty dependency array ensures this effect runs only once, when the component mounts.
  }, []);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]); // Captures the first selected file
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file); // Append binary data to FormData

    const API_ENDPOINT = "http://127.0.0.1:8080/mri/images";

    try {
      const response = await axios.post(API_ENDPOINT, formData, {
        // It's good practice to explicitly set the Content-Type header,
        // but Axios/browser often handle this automatically for FormData.
        headers: {
          "Content-Type": "multipart/form-data",
        },
        // You can also add an onUploadProgress callback here for a progress bar
      });

      // 3. Handle the successful (asynchronous) response
      //const fname = response.data.filename
    } catch (error) {
      console.error("Error saving data:", error);
    }
  };

  const renderIfItems = (items) => {
    if (items.length > 0) {
      return (
        <ul>
          {items.map((item) => (
            <li key={item} className="card-item">
              {item}
            </li>
          ))}
        </ul>
      );
    } else {
      return <p>No items found.</p>;
    }
  };
  return (
    <>
      <form className="row" method="post" onSubmit={handleSubmit}>
        <div className="col-6">
          <input
            type="file"
            name="fileMRI"
            id="file"
            className="form-control"
            onChange={handleFileChange}
            required
          />
        </div>
        <div className="col-6">
          <button className="btn btn-success" type="submit">
            Upload
          </button>
        </div>
      </form>

      <div className="row">
        <div className="card col-8 m-2">{renderIfItems(items)}</div>
      </div>
    </>
  );
}

export default PoolOfImages;
