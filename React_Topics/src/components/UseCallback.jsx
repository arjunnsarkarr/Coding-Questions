import React, { useState, useCallback } from "react";

const UseCallback = () => {
  const [count, setCount] = useState(0);

  // Without useCallback, this function would be recreated on every render.
  // With useCallback, it's only recreated when `count` changes.
  const handleClick = useCallback(() => {
    console.log("Button clicked!");
  }, [count]);

  return (
    <div>
      <h1>Count: {count}</h1>
      <button onClick={() => setCount(count + 1)}>Increment Count</button>
      <button onClick={handleClick}>Click Me</button>
    </div>
  );
};

export default UseCallback;
