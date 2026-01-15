import { useState } from "react";
import ImagesContainer from "./ImagesContainer";
import UploadImages from "./UploadImages";

function ImagesWorkspace() {
    const [refreshKey, setRefreshKey] = useState(0);
    const handleUploadSuccess = () => {
        setRefreshKey(refreshKey + 1);
    }
  return (
    <>
      <UploadImages onUploadSuccess={handleUploadSuccess}></UploadImages>
      <ImagesContainer refreshTrigger={refreshKey}></ImagesContainer>
    </>
  );
}

export default ImagesWorkspace;
