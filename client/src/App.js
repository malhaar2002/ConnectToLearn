import "./App.css";
import { useState, useEffect } from "react";

function App() {
  const [data, setData] = useState([{}]);

  useEffect(() => {
    fetch("/message")
      .then((res) => res.json())
      .then((data) => {
        setData(data);
        console.log(data);
      });
  }, []);

  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);

  const handleSend = async () => {
    const response = await fetch("/message", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: input }),
    });
    setMessages([
      ...messages,
      {text: input, isUser: true},
      {text: response.data, isUser: false}
    ]);
    setInput("");
    console.log(response.data)
  };

  return (
    <div className="App">
      <div className="chat">
        <div className="user-message">This is a user message</div>
        <div className="bot-message">This is a bot message</div>
      </div>

      <div className="input-container">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
        />
        <button onClick={handleSend}>Send</button>
      </div>
    </div>
  );
}

export default App;
