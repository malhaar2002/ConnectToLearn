import { createChatBotMessage } from 'react-chatbot-kit';

const botName = 'ConnectToLearn';
const initialMessage = `Hello there! I am ${botName}, and I am here to help you make the best of your projects. I am designed to leverage your completed courses, performance records, and areas of curiosity to suggest relevant projects. I can also connect you with the right people who can help validate and execute these projects, including faculty members, founders, NGOs, and organizations. Do you already have a specific project idea or research topic in mind? If yes, please provide a brief description.`;

const config = {
  initialMessages: [createChatBotMessage(initialMessage)],
  botName: botName,
};

export default config;