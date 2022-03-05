from flask import Flask, jsonify, redirect, render_template, request, url_for, Response


app = Flask(__name__)


comment_section = [{'user_name': 'Cross Cultural',
    'comment_id': '0',
    'comment': 'Most perfect tutorial ever. Very detailed. Finally I  learned Docker.'},
    {'user_name': 'Nabajyoti Nath',
    'comment_id': '1',
    'comment': 'Reall-y amazing !!! The best thing about this tutorial is that it not only covers all the concevpts of Docker, it also shows how it ties back with CI/CD pipeline.'},
    {'user_name': 'Jay lora',
    'comment_id': '2',
    'comment': 'A wise man once said, "Nana is the greatest thing since sliced bread."'},
    {'user_name': 'Калёная Сталь',
    'comment_id': '3',
    'comment': 'Finnaly, clear english tutorial'},
    {'user_name': 'Joselet K Devasia',
    'comment_id': '4',
    'comment': 'No words. Just amazing!'}
    ]

@app.route("/")
def index():
    return "Welcome to the comment section <h1>COMMENT SECTION</h1>"


@app.route("/comment_section", methods = ['GET'])
def get():
    return jsonify({'comment_section': comment_section})

@app.route("/comment_section/<int:comment_id>", methods = ['GET'])
def get_comment(comment_id):
    return jsonify({'comment': comment_section[comment_id]})

@app.route("/newcomment", methods = ['POST','GET'])
def create_comment():
    if request.method == 'POST':
        username = request.form['username']
        comment = request.form['comment']

        if username and comment:
            comment_section.append(username)
            comment_section.append(comment)

        return jsonify({'comment_section': comment_section})
      
    else:

        return render_template('newcomment2.html')
    


    



if __name__ == "__main__":
    app.run(debug=True)
