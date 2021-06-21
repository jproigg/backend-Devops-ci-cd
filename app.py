import os
from flask import Flask, jsonify, request, Response, render_template 
from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson import json_util
from bson.objectid import ObjectId

app = Flask(__name__)

#data base congiguration

app.config['MONGO_URI'] = 'mongodb://localhost:27017/pythonmongodb'

mongo = PyMongo(app)

democlient = MongoClient()
myclient = MongoClient('mongodb',27017)
mydb = myclient["pythonmongodb"]
mycoll=mydb["users"]

#home page route

@app.route("/")
def index():
    return "Welcome to the <h1>COMMENT SECTION</h1>"

#add new comment route
@app.route('/newcomment', methods=['POST','GET'])
def create_comment():
    if request.method == 'POST':

        username = request.form.get('username')
        comment = request.form.get('comment')

        if username and comment:
            id = mongo.db.users.insert(
            {'username': username, 'comment': comment}
            )
        response = jsonify({
            '_id': str(id),
            'username': username,
            'comment': comment
        })
        return render_template('newcomment.html')


    else:

        return render_template('newcomment.html')

#view comments in json file

@app.route("/comment_section", methods = ['GET'])
def get_comment_section():
    comment_section = mongo.db.users.find()
    response = json_util.dumps(comment_section)
    return response

#delete comment from data base

@app.route('/delete/<id>')
def delete_comment(id):
    mongo.db.users.delete_one({'_id': ObjectId(id)})
    response = jsonify({'message': 'comment' + id + ' Deleted Successfully'})
    return response



if __name__ == "__main__":
    app.run(host='0.0.0.0', port= 5000)

#Comment section dictionaries

'''comment_section = [{'user_name': 'Cross Cultural',
    'comment_id': '0',
    'comment': 'Most perfect tutorial ever. Very detailed. Finally I  learned Docker.'},
    {'user_name': 'Nabajyoti Nath',
    'comment_id': '1',
    'comment': 'Reall-y amazing !!! The best thing about this tutorial is that it not only covers all the concepts of Docker, it also shows how it ties back with CI/CD pipeline.'},
    {'user_name': 'Jay Flora',
    'comment_id': '2',
    'comment': 'A wise man once said, "Nana is the greatest thing since sliced bread."'},
    {'user_name': 'Калёная Сталь',
    'comment_id': '3',
    'comment': 'Finnaly, clear english tutorial'},
    {'user_name': 'Joselet K Devasia',
    'comment_id': '4',
    'comment': 'No words. Just amazing!'}
    ]'''