# -*- coding: utf-8 -*-
from datetime import datetime
from pathlib import Path
import shutil

import pytz as pytz
from flask_sqlalchemy import SQLAlchemy

from config import SQLITE_DATABASE_NAME, SQLITE_DATABASE_BACKUP_NAME

db = SQLAlchemy()


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(512), nullable=False)
    text = db.Column(db.String(512), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           default=lambda: datetime.now().astimezone(pytz.timezone('Europe/Moscow')))


def db_init(app):
    posts = [{"name": "testName", "text": "tesText"}]

    # Check if db file already exists. If so, backup it
    db_file = Path(SQLITE_DATABASE_NAME)
    if db_file.is_file():
        shutil.copyfile(SQLITE_DATABASE_NAME, SQLITE_DATABASE_BACKUP_NAME)

    with app.app_context():
        # Init DB
        db.session.commit()  # https://stackoverflow.com/questions/24289808/drop-all-freezes-in-flask-with-sqlalchemy
        db.drop_all()
        db.create_all()

        # Create Data Base
        for q in posts:
            print(q)
            tq = Post(name=q['name'], text=q['text'])
            db.session.add(tq)
            db.session.commit()
