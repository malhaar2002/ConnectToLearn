from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain import OpenAI
from langchain.memory import ConversationBufferMemory
from config import OPENAI_API_KEY


template = """You are expert at getting the main point of a discussion, I will be passing you a conversation between ai and person. Go through it and understand the discussion between the ai and the human. Understand the project,or research that was suggested by the ai to the student and then from come up with a 5 - 10 words long summary of the discussion that says recommend a professor for {{the topic of discussion}}. For example, if the discussion is about web-development, the summary will like ""Recommend a professor to learn about web-development from""

this is the conversation {input}:
"""

prompt = PromptTemplate(input_variables=["input"], template=template)

summary_chain = LLMChain(
    llm=OpenAI(model="gpt-4"),
    prompt=prompt,
    verbose=True,
)

user ="""AI: Hello! Welcome to ConnectToLearn. Our main goal is to assist you in identifying and executing projects that align with your interests and skills. To begin, I have a question for you. Do you already have a specific project idea or research topic in mind? If yes, please provide a brief description.
Human: I am currently learning web-development and I want to work on interesting project to improve my programming skills 
Chatbot
That's great! Working on projects is a fantastic way to apply what you've learned and gain hands-on experience. Here's a step-by-step guide to help you execute a web development project:

1. **Define the Project**: Start by defining what you want your web application to do. This could be anything from a personal blog to a weather application. Write down the features you want to include.

2. **Design the Layout**: Sketch how you want your website to look. This should include the arrangement of elements, color schemes, and any interactive features. There are several online tools available for this, such as Sketch or Adobe XD.

3. **Create a Project Plan**: Break down your project into smaller tasks. For example, setting up your development environment, designing the homepage, creating user authentication, etc. This will make the project more manageable and help you track your progress.

4. **Set Up Your Development Environment**: Depending on your project, this could include installing a code editor (like VS Code), setting up a server, or downloading relevant libraries and frameworks.

5. **Start Coding**: Begin by developing the basic structure of your website with HTML. Next, style your website using CSS. Finally, use JavaScript to make your website interactive.

6. **Test Your Application**: Make sure to test your application regularly. This includes checking the design on different devices and browsers and testing any functionalities to ensure they work correctly.

7. **Deploy Your Website**: Once you're satisfied with your website, it's time to deploy it. There are several free hosting platforms available, such as Netlify or GitHub Pages.

8. **Get Feedback and Iterate**: After deployment, get feedback from users and use this to improve your website. Web development is an iterative process, and there's always room for improvement.

Remember, the key to improving your programming skills is to practice consistently. Don't be discouraged if you encounter difficulties along the way, every problem is a learning opportunity. Good luck with your project!
Human: Hello 
AI: Hello! Welcome to ConnectToLearn. Our main goal is to assist you in identifying and executing projects that align with your interests and skills. To begin, I have a question for you. Do you already have a specific project idea or research topic in mind? If yes, please provide a brief description.
Human: I am currently learning web-development and I want to work on interesting project to improve my programming skills 
AI: That's great! Working on projects is a fantastic way to apply what you've learned and gain hands-on experience. Here's a step-by-step guide to help you execute a web development project:

1. **Define the Project**: Start by defining what you want your web application to do. This could be anything from a personal blog to a weather application. Write down the features you want to include.

2. **Design the Layout**: Sketch how you want your website to look. This should include the arrangement of elements, color schemes, and any interactive features. There are several online tools available for this, such as Sketch or Adobe XD.

3. **Create a Project Plan**: Break down your project into smaller tasks. For example, setting up your development environment, designing the homepage, creating user authentication, etc. This will make the project more manageable and help you track your progress.

4. **Set Up Your Development Environment**: Depending on your project, this could include installing a code editor (like VS Code), setting up a server, or downloading relevant libraries and frameworks.

5. **Start Coding**: Begin by developing the basic structure of your website with HTML. Next, style your website using CSS. Finally, use JavaScript to make your website interactive.

6. **Test Your Application**: Make sure to test your application regularly. This includes checking the design on different devices and browsers and testing any functionalities to ensure they work correctly.

7. **Deploy Your Website**: Once you're satisfied with your website, it's time to deploy it. There are several free hosting platforms available, such as Netlify or GitHub Pages.

8. **Get Feedback and Iterate**: After deployment, get feedback from users and use this to improve your website. Web development is an iterative process, and there's always room for improvement.

Remember, the key to improving your programming skills is to practice consistently. Don't be discouraged if you encounter difficulties along the way, every problem is a learning opportunity. Good luck with your project!"""

print(summary_chain({"input" : user}))