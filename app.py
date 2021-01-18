from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/question')
def question():
    page = request.args.get('page')
    question = db.questions.find_one({'idx':int(page)}, {'_id': False})
    answers = list(db.answers.find({'question_idx':int(page)}, {'_id': False}))
    return jsonify({'result': 'success', 'question': question, "answers":answers})

@app.route('/addAnswer')
def addAnswer():
    page = request.args.get('page')
    addAnswer = db.questions.find({'idx': int(page)}, {'_id': False})
    answers = list(db.answers.find({'desc': int(page)}, {'_id': False}))
    return jsonify({'result': 'success', "answers": answers})

@app.route('/makeAnswer')
def makeAnswer():
    page = request.args.get('page')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)
