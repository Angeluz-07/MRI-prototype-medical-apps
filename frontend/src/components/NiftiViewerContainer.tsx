import { useState, useEffect } from "react";
import axios from "axios";
import NiftiViewer from "./NiftiViewer";

type NiftiViewerContainerProps = {
  imgId: string;
};

function NiftiViewerContainer({ imgId }: NiftiViewerContainerProps) {
  const [imgBase64Code, setImgBase64Code] = useState<string>("");
  useEffect(() => {
    const fetchStringValue = async (id: string) => {
      // Replace this with your actual API endpoint and logic for the single value
      //const INITIAL_API_ENDPOINT = 'http://127.0.0.1:8080/mri/images'
      const API_ENDPOINT = `http://127.0.0.1:8080/mri/results/${id}`;
      console.log(`📡 Hitting endpoint: ${API_ENDPOINT}`);

      try {
        // Simulate network delay and data response
        const response = await axios.get(API_ENDPOINT);

        //return response.data.basestr;
        setImgBase64Code(response.data.basestr);
      } catch (error) {
        console.error(`Error fetching strValue for ${id}:`, error);
        return null;
      }
    };
    fetchStringValue(imgId)
  }, [imgId]);

  return (
    <>
      <NiftiViewer imgBase64Code={imgBase64Code}></NiftiViewer>
    </>
  );
}

export default NiftiViewerContainer;
