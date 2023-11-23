from flask import Flask, render_template

app = Flask(__name__)

app.route('/')
def load():
	print("The page is loaded!!11")
	return render_template('index.html')

if __name__ == "__main__":
	app.run()