import React from "react";

const ActionProvider = ({ createChatBotMessage, setState, children }) => {

  const handleMessage = (botResponse) => {
    const botMessage = createChatBotMessage(botResponse);
    setState((prev) => ({
      ...prev,
      messages: [...prev.messages, botMessage],
    }));
  };

  const handleProjectRecommender = () => {
    sessionStorage.setItem("model", "project_recommender");
    handleMessage("Great! Do you already have a specific project idea or research topic in mind? If yes, please provide a brief description");
  };

  const handleMentorRecommender = () => {
    sessionStorage.setItem("model", "mentor_recommender");
    handleMessage("Great! Please describe your idea / field of interest and I'll try to find the right people for you to connect with");
  };

  const handleOptionNotSelected = () => {
    createChatBotMessage("Please select one of the options to proceed.", {
      widget: "options",
    });
    setState((prev) => ({
      ...prev,
      messages: [...prev.messages],
    }));
  };

  return (
    <div>
      {React.Children.map(children, (child) => {
        return React.cloneElement(child, {
          actions: {
            handleMessage,
            handleProjectRecommender,
            handleMentorRecommender,
            handleOptionNotSelected,
          },
        });
      })}
    </div>
  );
};

export default ActionProvider;
