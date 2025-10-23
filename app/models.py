from app import db  # from flask_sqlalchemy

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300))
    author = db.Column(db.String(200))
    published_date = db.Column(db.String(100))
    isbn = db.Column(db.String(50))
    price = db.Column(db.Float)


