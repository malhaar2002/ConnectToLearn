from flask import Flask, request
from research import get_research

app = Flask(__name__)

@app.route('/message', methods=['POST'])
def home():
	project = request.get_json()['message']
	result = get_research(project)
	return result

if __name__ == '__main__':
	app.run(debug=True)