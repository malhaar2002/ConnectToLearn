from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/api', methods=['GET', 'POST'])
def api():
	if request.method == 'POST':
		data = {"result": "success"}
		return jsonify(data)
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)