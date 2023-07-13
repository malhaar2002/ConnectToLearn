import openai
import sys
import json
# sys.path.append('../')
# from config import OPENAI_API_KEY

# Set up your OpenAI GPT API credentials
openai.api_key = "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"

def get_research(project):

    # Generate additional information using the GPT API
    prompt = f"""I want to build {project}. I want you to scrape the internet and give me any relevant information. The output should be in the format given below in double backticks
    ``
    {{
        "research": [],
        "competitor products": [],
    }}
    ``
    Give only a json response without the backticks. Do not give any anything else.
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        n=1,  # Specify the number of completions you want
        stop=None,
    )

    return json.loads(response["choices"][0]["text"])

if __name__ == '__main__':
    print(get_research("a platform that can help students pursue projects of interest by connecting them with mentors and other students"))