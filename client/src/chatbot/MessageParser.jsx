import React from 'react';
import { useState } from 'react';

const MessageParser = ({ children, actions }) => {

  const [message, setMessage] = useState('');

  const sendMessageToBackend = async () => {
    try {
      const response = await fetch('/message', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user_message: message }),
      });

      const data = await response.json();
      console.log(data)
      return data;
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const parse = async (message) => {
    setMessage(message);
    const botResponse = await sendMessageToBackend()
    actions.handleMessage(botResponse.bot_message);
  };

  return (
    <div>
      {React.Children.map(children, (child) => {
        return React.cloneElement(child, {
          parse: parse,
          actions
        });
      })}
    </div>
  );
};

export default MessageParser;