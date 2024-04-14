import React, { useState } from "react";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import SendIcon from "@mui/icons-material/Send";

import "./App.css";

function App() {
  const [stockName, setStockName] = useState("");

  const submit = (e) => {
    e.preventDefault();
    console.log(stockName);
  };

  return (
    <div className="App">
      <div className="navigationBar">
        <form onSubmit={submit}>
          <TextField
            hiddenLabel
            id="filled-hidden-label-small"
            variant="filled"
            size="small"
            className="searchBar"
            placeholder="Enter Stock"
            name="searchStock"
            onChange={(e) => setStockName(e.target.value)}
            value={stockName}
            type="text"
          />
          <Button
            className="searchButton"
            variant="contained"
            size="large"
            type="submit"
          >
            <SendIcon />
          </Button>
        </form>
      </div>
    </div>
  );
}

export default App;
