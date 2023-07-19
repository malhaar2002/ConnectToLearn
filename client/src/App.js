import "./App.css";
import { useState, useEffect } from "react";
import ChatBot from "react-chatbot-kit";
import 'react-chatbot-kit/build/main.css'
import ActionProvider from "./chatbot/ActionProvider";
import MessageParser from "./chatbot/MessageParser";
import config from "./chatbot/config";

function App() {
  const [data, setData] = useState([{}]);

  // useEffect(() => {
  //   fetch("/message")
  //     .then((res) => res.json())
  //     .then((data) => {
  //       setData(data);
  //       console.log(data);
  //     });
  // }, []);

 return (
  <div className="App">
    <div style={{ maxWidth: "300px" }}>
      <ChatBot
        config={config}
        actionProvider={ActionProvider}
        messageParser={MessageParser}
      />
    </div>
  </div>
 ) 
}

export default App;
