#Sends book data as JSON. 📦

from flask import Blueprint, jsonify, request
from app.models import Book

api_bp = Blueprint('api', __name__)

@api_bp.route("/api/books")
def api_books():
    q = request.args.get('q', '', type=str)
    query = Book.query
    if q:
        query = query.filter(
            (Book.title.ilike(f"%{q}%")) | (Book.author.ilike(f"%{q}%"))
        )
    books = query.all()
    return jsonify([
        {
            "title": b.title,
            "author": b.author,
            "published_date": b.published_date,
            "isbn": b.isbn,
            "price": b.price
        } for b in books
    ])