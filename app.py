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
myclient = MongoClient (host='mongodb',
                        port=27017, 
                        username='mongoadmin', 
                        password='password',
                        authSource="admin")
mydb = myclient["pythonmongodb"]
mycoll=mydb["users"]


#home page route

@app.route("/")
def index():
    return "Welcome to the <h1>COMMENT SECTION</h1>"

#add new comment route
@app.route('/newcomment', methods=['GET','POST'])
def create_comment():
    if request.method == 'POST':

        username = request.form.get('username')
        comment = request.form.get('comment')

        if username and comment:
            id = mongo.db.users.insert_one(
            {'username': username, 'comment': comment}
            )
        response = jsonify({
            '_id': str(id),
            'username': username,
            'comment': comment
        })
        return response


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
    app.run(host='0.0.0.0', port=5000, debug=True)





    