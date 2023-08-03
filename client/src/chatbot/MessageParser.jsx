import React from 'react';

const MessageParser = ({ children, actions }) => {

  const parse = async (message) => {
    let botResponse = { bot_message: "Sorry, there was some error." }

    // send a message to the server and update botResponse with the response
    try {
      const response = await fetch('/message', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user_message: message }),
      });
      botResponse = await response.json();
    } catch (error) {
      console.error('Error:', error);
    }

    // call the handleMessage function from the ActionProvider component
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