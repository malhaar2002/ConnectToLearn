import React from 'react';

const MessageParser = ({ children, actions }) => {

  const parse = async (message) => {
    const userID = sessionStorage.getItem('userID');
    const model = sessionStorage.getItem('model');
    let botResponse = { bot_message: "Sorry, there was some error." }

    // check if model option selected
    if (model === null) {
      actions.handleOptionNotSelected();
    }
    else {
      let url = `/api/${userID}/${model}`;

      // send a message to the server and update botResponse with the response
      try {
        const response = await fetch(url, {
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
    }
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