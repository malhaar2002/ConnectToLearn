from flask import Flask, request
import openai.error
from project_recommder_model import create_llm_chain 

app = Flask(__name__)
llm_chains = {}

@app.route('/<string:userID>/message', methods=['POST'])
def home(userID):
	user_input = request.get_json()["user_message"]
	llm_chain = llm_chains.get(userID, None)
	if llm_chain is None:
		llm_chain = create_llm_chain()
		llm_chains[userID] = llm_chain
	try:
		result = llm_chain.predict(human_input = user_input)
	except openai.error.InvalidRequestError:
		result = "Sorry, I have reached the limit of our conversation (I am a bit of an introvert). Please start a new conversation. If you are the developer, please check the logs for any errors."
	except:
		result = "Sorry, something went wrong. If you are the developer, please check the logs for errors."
	json_result = {"bot_message": result}
	return json_result

@app.route('/<string:userID>/leave', methods=['POST'])
def handle_leave(userID):
    if userID in llm_chains:
        del llm_chains[userID]
    return "User left"


if __name__ == '__main__':
	app.run(debug=True)