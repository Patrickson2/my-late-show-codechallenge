from flask_sqlalchemy import SQLAlchemy



class Episode(db.Model):
    __tablename__ = 'episodes'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10))
    number = db.Column(db.Integer)