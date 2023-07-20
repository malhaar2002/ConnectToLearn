from flask import Flask, request
from project_recommder_model import llm_chain

app = Flask(__name__)

@app.route('/message', methods=['POST'])
def home():
	user_input = request.get_json()["user_message"]
	result = llm_chain.predict(human_input = user_input)
	json_result = {"bot_message": result}
	return json_result

if __name__ == '__main__':
	app.run(debug=True)