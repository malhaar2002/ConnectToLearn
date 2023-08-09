from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain import OpenAI
from langchain.memory import ConversationBufferMemory
from config import OPENAI_API_KEY
from langchain.chat_models import ChatOpenAI
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
import re

# function to remove unecessary pattern


def remove_special_characters(text):
    # Regular expression to match all characters except A-Z, a-z, 0-9, spaces, and newlines
    pattern = r'[^A-Za-z0-9 \n]'

    # Use re.sub() to remove all non-alphanumeric characters
    cleaned_text = re.sub(pattern, '', text)

    return cleaned_text

# model


def model():
    template = """As an expert in grasping the main points of discussions, your task is to analyze the conversation between AI and a person. The conversation will involve a project or research suggested by the AI to the student. After understanding the discussion, provide a concise 5 to 10-word summary that recommends a suitable professor for the topic. The example below shows the format, and the only thing that will change in the example is what they are recommending.

    For example, if the discussion is about web development, your summary should be: "Recommend a professor for web development."

    Human: {human_input}
    """
    prompt = PromptTemplate(
        input_variables=["human_input"], template=template
    )
    return LLMChain(
        llm=OpenAI(),
        prompt=prompt,
        verbose=True,
    )


def main():
    llm_chain = model()

    text = "Conversation"
    remove_special_characters(text)
    llm_chain.predict(human_input=text)


if __name__ == "__main__":
    main()
