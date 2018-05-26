# coding=utf-8

# serve.py

from flask import Flask, render_template, url_for
from stasiroyal3 import stasi_bot

# creates a Flask application, named app
app = Flask(__name__)


@app.route("/")
# a route where we will display a welcome message via an HTML template
def hello():
    return render_template('index.html')


@app.route('/data')
def script_output():
    data_list = stasi_bot()
    """
    formatted = []
    for item in data_list:
        print(item)
        line = "{rank}, {playerName}, {playerID}, {donations}, {crowns}, {noob}".format(**item)
        formatted.append(line)
    output = "\n".join(formatted)
    """
    data_list.sort(key=lambda x: int(x['crowns']))
    data_list.reverse()
    return render_template('data.html', output=data_list)


# run the application
if __name__ == "__main__":
    app.run(debug=False)
