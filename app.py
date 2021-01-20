from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
import uuid

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

@app.route('/save', methods=["POST"])
def save():
    idxs = request.form.getlist('answer_idxs[]')
    uuid_value= str(uuid.uuid1())
    result = {
        "uuid":uuid_value,
        "answer_idxs":idxs
    }
    db.result.insert_one(result)
    return jsonify({'result': 'success', 'uuid':uuid_value})

@app.route('/<uuid>', methods=["GET"])
def result(uuid):
    answer_idxs = db.result.find_one({"uuid":uuid})["answer_idxs"]
    sentence = ""
    for i in answer_idxs:
        sentence += db.answers.find_one({"answer_idx":int(i)})["desc"]
    return render_template('result.html', sentence=sentence)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)
