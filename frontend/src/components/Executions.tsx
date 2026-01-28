import { useState, useEffect } from "react";
import axios from "axios";

function Executions() {
  const [items, setItems] = useState<Array<string>>([]);
  const [file, setFile] = useState<string>("");

  useEffect(() => {
    const fetchItems = async () => {
      // A placeholder URL - **Replace this with your actual API endpoint**
      const API_URL = "http://127.0.0.1:8080/execution-details";

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
      <div >
        <table class="table">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">Algorithm Name</th>
              <th scope="col">Message</th>
              <th scope="col">Level</th>
              <th scope="col">Timestamp</th>
            </tr>
          </thead>
          <tbody>
            {items.map((item, index) => (
              <tr scope="row">
                <th scope="row">{index}</th>
                <td>{item.algorithm_name}</td>
                <td>{item.message}</td>
                <td>{item.level}</td>
                <td>{item.timestamp}</td>
              </tr>
            ))}
            <tr></tr>
          </tbody>
        </table>
      </div>
    </>
  );
}

export default Executions;
