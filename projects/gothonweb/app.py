from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_worldr():
	greeting = "Akhila"
	return f'Hello,{greeting}!'
if __name__ =="__main__":
	app.run()

