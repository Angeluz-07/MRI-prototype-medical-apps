import { useState, useEffect } from "react";
import Images from "./Images";
import axios from "axios";
type ImagesContainerProps = { 
  refreshTrigger: number
 };
function ImagesContainer({refreshTrigger}: ImagesContainerProps) {
  const [items, setItems] = useState<Array<string>>([]);

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

  }, [refreshTrigger]);

  return (
    <>
      <Images items={items}></Images>
    </>
  );
}

export default ImagesContainer;
