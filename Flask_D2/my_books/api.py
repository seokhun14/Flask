from flask.views import MethodView
from flask_smorest import Blueprint, abort
from my_books.schemas import BookSchema

blp = Blueprint("books", "books", url_prefix="/books", description="책 관리 API")

books = []
book_id_counter = 1

@blp.route("/")
class BookListResource(MethodView):  # ← 여기 MethodView 상속
    @blp.response(200, BookSchema(many=True))
    def get(self):
        return books

    @blp.arguments(BookSchema)
    @blp.response(201, BookSchema)
    def post(self, new_book):
        global book_id_counter
        new_book["id"] = book_id_counter
        book_id_counter += 1
        books.append(new_book)
        return new_book

@blp.route("/<int:book_id>")
class BookResource(MethodView):  # ← 여기 MethodView 상속
    @blp.response(200, BookSchema)
    def get(self, book_id):
        book = next((b for b in books if b["id"] == book_id), None)
        if not book:
            abort(404, message="Book not found")
        return book

    @blp.arguments(BookSchema)
    @blp.response(200, BookSchema)
    def put(self, updated_data, book_id):
        book = next((b for b in books if b["id"] == book_id), None)
        if not book:
            abort(404, message="Book not found")
        book.update(updated_data)
        return book

    @blp.response(204)
    def delete(self, book_id):
        global books
        before_count = len(books)
        books = [b for b in books if b["id"] != book_id]
        if len(books) == before_count:
            abort(404, message="Book not found")
        return ""
