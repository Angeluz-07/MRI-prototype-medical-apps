import { useState } from "react";
import ImagesContainer from "./ImagesContainer";
import UploadImages from "./UploadImages";
import InputsViewer from "./InputsViewer";

function ImagesWorkspace() {
    const [refreshKey, setRefreshKey] = useState(0);
    const handleUploadSuccess = () => {
        setRefreshKey(refreshKey + 1);
    }
  return (
    <>
      <UploadImages onUploadSuccess={handleUploadSuccess}></UploadImages>
      <ImagesContainer refreshTrigger={refreshKey}></ImagesContainer>
      <InputsViewer></InputsViewer>
    </>
  );
}

export default ImagesWorkspace;
