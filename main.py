import os
import json
from flask import Flask, abort, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/')
def get_all_posts():
    # strip off .md

    files = os.listdir('posts')
    files = [f.split('.')[0] for f in files]
    return json.dumps(files)

@app.route('/post/<post>')
def get_post(post):
    try:
        with open('posts/{}.md'.format(post)) as f:
            return f.read()
    except FileNotFoundError:
        abort(404)

# endpoint for posting blog posts
@app.route('/upload/<post>', methods=['POST'])
def post_post(post):
    try:
        with open('posts/{}.md'.format(post), 'w') as f:
            f.write(request.data)
        return 'OK'
    except FileNotFoundError:
        abort(404)

if __name__ == '__main__':
    app.run()

