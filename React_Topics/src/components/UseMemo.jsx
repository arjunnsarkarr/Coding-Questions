import React, { useMemo, useState } from "react";

const UseMemo = () => {
  const [count, setCount] = useState(0);
  const [num, setNum] = useState(5);

  function ExpensiveCalculation(num) {
    console.log("Calculating...");
    let result = 0;
    for (let i = 0; i < 100; i++) {
      result += num;
    }

    return result;
  }

  // useMemo will cache the result of ExpensiveCalculation
  const expensiveResult = useMemo(() => ExpensiveCalculation(num), [num]);

  return (
    <div>
      <h1>Count: {count}</h1>
      <button onClick={() => setCount(count + 1)}>Increase Count</button>

      <h2>Expensive Calculation Result: {expensiveResult}</h2>
      <button onClick={() => setNum(num + 1)}>Change Number</button>
    </div>
  );
};

export default UseMemo;
