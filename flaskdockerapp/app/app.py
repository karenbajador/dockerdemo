from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def mainpage():
	return "Hello Wonderful World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
