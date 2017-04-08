from flask import Flask, jsonify, abort
from datetime import datetime
import pytz
from sentence_ai import get_token, get_intent

app = Flask(__name__)


@app.route('/')
def homepage():
    the_time = datetime.now(pytz.timezone("Asia/Bangkok")).strftime("%A, %d %b %Y %I:%M %p")

    return """
    <h1>Welcome!! We are Estaurant.</h1>
    <p>It is currently {time}.</p>

    """.format(time=the_time)


@app.route('/intents/<sent>', methods=['GET'])
def process_sentence(sent):
    if len(sent) == 0:
        abort(500)

    tokens = get_intent(get_token(sent))
    return jsonify({'intent': tokens[0].name, 'keyword': tokens[1]})


@app.route('/tokenize/<sent>', methods=['GET'])
def tokenize_sentence(sent):
    if len(sent) == 0:
        abort(500)
    tokens = get_intent(get_token("อยากกินข้าวมันไก่เนื้อๆ"))
    print("Intent  : {}".format(tokens[0].name))
    print("Keyword : {}".format(tokens[1]))
    return jsonify({'intent': 'keyword', 'keyword': tokens})


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
