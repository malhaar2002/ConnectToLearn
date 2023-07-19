import React from 'react';

const ActionProvider = ({ createChatBotMessage, setState, children }) => {
  const handleMessage = (botResponse) => {
    const botMessage = createChatBotMessage(botResponse);
    setState((prev) => ({
      ...prev,
      messages: [...prev.messages, botMessage],
    }))
  }

  return (
    <div>
      {React.Children.map(children, (child) => {
        return React.cloneElement(child, {
          actions: {handleMessage},
        });
      })}
    </div>
  );
};

export default ActionProvider;