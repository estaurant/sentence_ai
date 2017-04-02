from flask import Flask, jsonify, abort
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Welcome!! We are Estaurant.</h1>
    <p>It is currently {time}.</p>

    """.format(time=the_time)

@app.route('/intents/<sent>', methods=['GET'])
def process_sentence(sent):
    if len(sent) == 0:
        abort(500)
    return jsonify({'intent': 'keyword', 'keyword':sent})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)