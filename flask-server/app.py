from flask import Flask, request
import openai.error
from project_recommder_model import llm_chain

app = Flask(__name__)

@app.route('/message', methods=['POST'])
def home():
	user_input = request.get_json()["user_message"]
	try:
		result = llm_chain.predict(human_input = user_input)
	except openai.error.InvalidRequestError:
		result = "Sorry, I have reached the limit of our conversation (I am a bit of an introvert). Please start a new conversation. If you are the developer, please check the logs for any errors."
	except:
		result = "Sorry, something went wrong. If you are the developer, please check the logs for errors."
	json_result = {"bot_message": result}
	return json_result

if __name__ == '__main__':
	app.run(debug=True)