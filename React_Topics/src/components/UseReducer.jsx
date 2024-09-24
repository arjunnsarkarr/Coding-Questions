import React, { useReducer } from "react";

const UseReducer = () => {
  
    // Step 1: Define the reducer function
  function reducer(state, action) {
    if (action.type === "increment") {
      return { count: state.count + 1 };
    } else if (action.type === "decrement") {
      return { count: state.count - 1 };
    } else {
      return state;
    }
  }

  // Step 2: Initialize useReducer with the reducer function and the initial state
  const initialState = { count: 0 };
  const [state, dispatch] = useReducer(reducer, initialState);

  return (
    <div>
      <p>Count: {state.count}</p>

      {/* Step 3: Use dispatch to send actions to the reducer */}
      <button onClick={() => dispatch({ type: "increment" })}>Increment</button>
      <button onClick={() => dispatch({ type: "decrement" })}>Decrement</button>
    </div>
  );
};

export default UseReducer;
