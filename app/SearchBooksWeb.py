
#Displays books on HTML web page

from flask import Blueprint, render_template, request
from app.models import Book

main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def home():
    page = request.args.get('page', 1, type=int)  # Get the current page number
    q = request.args.get('q', '', type=str)  # Get the search query
    query = Book.query
    if q:  # Filter books by title or author if a search query is provided
        query = query.filter(
            (Book.title.ilike(f"%{q}%")) | (Book.author.ilike(f"%{q}%"))
        )
    books = query.paginate(page=page, per_page=10)  # Paginate the results
    return render_template("index.html", books=books)