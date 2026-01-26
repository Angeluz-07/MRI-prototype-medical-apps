import { useState, useEffect } from "react";
import axios from "axios";

function Executions() {
  const [items, setItems] = useState<Array<string>>([]);
  const [file, setFile] = useState<string>("");

  useEffect(() => {
    const fetchItems = async () => {
      // A placeholder URL - **Replace this with your actual API endpoint**
      const API_URL = "http://127.0.0.1:8080/executions";

      try {
        const response = await axios.get(API_URL);
        // Assuming the response data is an array of objects
        setItems(response.data.items);
      } catch (err) {
        console.error("Error fetching data:", err);
      }
    };

    fetchItems();

  }, []);



  return (
    <>
      <div className="col-4">
          {items.map((item) => (
            <li >{item.id} - {item.message} - {item.timestamp}</li>
          ))}
      </div>
    </>
  );
}

export default Executions;
