import { useState } from "react";
//todo: consider rename to ListImages
type ImagesProps = {
  items: Array<string>;
};

function Images({ items }: ImagesProps) {

  const renderIfItems = (items: Array<string>) => {
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
      <div className="row">
        <div className="card col-8 m-2">{renderIfItems(items)}</div>
      </div>
    </>
  );
}

export default Images;
