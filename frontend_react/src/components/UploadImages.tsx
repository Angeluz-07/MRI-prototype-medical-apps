import { useState, useEffect } from "react";
import axios from "axios";

type UploadImagesProps = {
  onUploadSuccess: () => void;
};

function UploadImages({ onUploadSuccess }: UploadImagesProps) {
  const [file, setFile] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]); // Captures the first selected file
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) return;

    const formData = new FormData();
    formData.append("fileMRI", file); // Append binary data to FormData

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
      onUploadSuccess();
      //const fname = response.data.filename
    } catch (error) {
      console.error("Error saving data:", error);
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
    </>
  );
}

export default UploadImages;
