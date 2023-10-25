from . import reading_blueprint as book
from flask import request
from flask_jwt_extended import jwt_required, current_user
from ..models import User, Book
from ..utils import bad_request_if_none

@book.post("/new")
@jwt_required()
def handle_create_reading():
    body = request.json

    if body is None:
        response = {
            "message": "invalid request"
        }
        return response, 400
    
    title = body.get("title")
    if title is None or title == "":
        response = {
            "message": "invalid request"
        }
        return response, 400

    description = body.get("description")
    if description is None or description == "":
        response = {
            "message": "invalid request"
        }
        return response, 400

    existing_book= read.query.filter_by(title=title).one_or_none()
    if existing_book is not None:
        response = {
            "message": "that title is already in use"
        }
        return response, 400

    read = read(title=title, description=description, created_by=current_user.id)
    read.create()

    response = {
        "message": "successfully created quiz",
        "book": read.to_response()
    }
    return response, 201

@book.get("/all")
# @jwt_required()
def handle_get_all_book():
    books = book.query.all()
    response = {
        "message": "books retrieved",
        "books": [book.to_response() for book in books]
    }
    return response, 200

@book.get("/mine")
@jwt_required()
def handle_get_my_books():
    books = book.query.filter_by(created_by=current_user.id).all()
    response = {
        "message": "book retrieved",
        "books": [book.to_response() for book in books]
    }
    return response, 200

@book.get("/<book_id>")
@jwt_required()
def handle_get_one_book(book_id):
    book= book.query.filter_by(id=book_id).one_or_none()
    if book is None:
        response = {
            "message": "book does not exist"
        }
        return response, 404

    response = {
        "message": "book found",
        "book": book.to_response() 
    }
    return response, 200

@book.delete("/delete-book/<book_id>")
@jwt_required()
def handle_delete_book(book_id):
    book = book.query.filter_by(id=book_id).one_or_none()
    if book is None:
        response = {
            "message": "book does not exist"
        }
        return response, 404

    if book.created_by != current_user.id:
        response = {
            "message":"you cant delete someone elses book"
        }
        return response, 401
    
    book.delete()

    response = {
        "message": f"book {book.id} deleted"
    }
    return response, 200

@book.post("/add-book/<book_id>")
# @jwt_required()
def handle_add_book(book_id):
    body = request.json

    print(body)
    if body is None:
        response = {
            "message": "invalid request"
        }
        return response, 400

    book = book.query.filter_by(id=book_id).one_or_none()
    if book is None:
        response = {
            "message": "book not found"
        }
        return response, 404
    
    print(book.created_by)
    # print(current_user.id)
 
@book.put("/update/book/<book_id>")
@jwt_required()
def handle_update_book(book_id):
    body = request.json

    book = book.query.filter_by(id=book_id).one_or_none()
    if book is None:
        response = {
            "message": "not found"
        }
        return response, 404

    if book.created_by != current_user.id:
        response = {"message":"no sir/maam"}
        return response, 401
    

    book.title = body.get("title", book.title)
    book.description = body.get("description", book.description)
    
    book.update()

    response = {
        "message": "book updated",
        "books": book.to_response()
    }
    return response, 200

