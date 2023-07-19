from flask import Flask, request
from research import get_research

app = Flask(__name__)

@app.route('/message', methods=['POST'])
def home():
	project = request.get_json()["message"]
	with open("log.txt", "w") as f:
		f.write(project + "\n")
	result = get_research(project)
	# with open("log.txt", "a") as f:
	# 	f.write(result + "\n")
	return result

if __name__ == '__main__':
	app.run(debug=True)