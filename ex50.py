from flask import flask
app = Flask(__name__)
@app.route('/')
def hello_world():
	greeting = "world"
	return f'Hello, {greeting}!'
if __name__ == "__main__":
	app.run()
