import sys

from flask import Flask, render_template, request, redirect

from config import SQLITE_DATABASE_NAME
from models import db_init, db, Post

app = Flask(__name__)

# SQLAlchimy config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + SQLITE_DATABASE_NAME

# Init Database
db.app = app
db.init_app(app)


@app.route('/', methods = ['POST', 'GET'])
def index():
    if (request.method == "POST"):
        name = request.form['name']
        text = request.form['text']
        tq = Post(name=name, text=text)
        db.session.add(tq)
        db.session.commit()
        return redirect(request.path, code=302)
    return render_template("index.html", posts=Post.query.all())


if __name__ == "__main__":

    if len(sys.argv) > 1:
        if sys.argv[1] == "init":
            db_init(app)

    app.run(host="0.0.0.0", port=5000)
