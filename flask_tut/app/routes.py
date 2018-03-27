import os
import glob

from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Josh'}

    readmes = glob.glob("/home/jvita/scripts/100_days_of_code/*/README")

    posts = [{'title': os.path.split(os.path.split(f)[0])[-1],
              'body': open(f, 'r').readlines()} for f in readmes]

    return render_template('index.html', title='Josh\'s #100DaysOfCode',
                           user=user, posts=posts)

def make_tree(path):

    tree = dict(name=os.path.basename(path), children=[])

    try: lst = os.listdir(path)
    except OSError:
        pass #ignore errors
    else:
        for name in lst:
            fn = os.path.join(path, name)
            if os.path.isdir(fn):
                tree['children'].append(make_tree(fn))
            else:
                with open(fn) as f:
                    contents = f.read()
                tree['children'].append(dict(name=name, contents=contents))
    return tree
