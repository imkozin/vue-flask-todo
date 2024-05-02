from flask import Flask, jsonify, request
from flask_cors import CORS
from sqlalchemy import text
from dotenv import load_dotenv
import os
from db import db, init_db
from models import Task

load_dotenv()

app = Flask(__name__)

CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
app.config["JWT_SECRET_KEY"] = os.environ.get("SECRET_KEY")


init_db(app)


@app.route("/test_db_connection")
def test_db_connection():
    try:
        result = db.session.execute(text("SELECT 1"))
        return "Database connection is working."
    except Exception as e:
        return f"Error: {str(e)}"


@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()

    task_list = []
    for task in tasks:
        task_data = {"task_id": task.task_id, "title": task.title, "text": task.text}

        task_list.append(task_data)

    return jsonify(task_list)


@app.route("/api/add-task", methods=["POST"])
def add_product():
    data = request.get_json()

    title = data.get("title")
    text = data.get("text")

    if not text or not title:
        return jsonify({"error": "Title and text cannot be empty!"}), 400

    if len(title) > 30:
        return jsonify({"error": "Task title is too long! (max. 30 symbols)"}), 400

    if len(text) > 50:
        return jsonify({"error": "Text content can contain till 50 symbols"}), 400

    new_task = Task(title=title, text=text)
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"message": "Task added successfully"}), 201


@app.route("/api/edit-task/<int:id>", methods=["PUT"])
def edit_task(id):
    task = Task.query.get(id)

    if task is not None:
        data = request.get_json()
        new_title = data.get("title")
        new_text = data.get("text")

        if new_title is not None and new_text is not None:
            task.title = new_title
            task.text = new_text
            db.session.commit()
            return jsonify({"message": "Task updated successfully"}), 200
        else:
            return jsonify({"error": "Title and text fields cannot be empty"}), 400
    else:
        return jsonify({"error": "Task not found"}), 404


@app.route("/api/delete-task/<int:id>", methods=["DELETE"])
def delete_task(id):

    task = Task.query.get(id)

    if task is not None:
        db.session.delete(task)
        db.session.commit()
        return jsonify({"message": "Task deleted successfully!"}), 200
    else:
        return jsonify({"message": "Task not found"}), 404


# @app.route('/api/get-product/<int:id>', methods=['GET'])
# def get_product_data(id):
#     product = Product.query.get(id)

#     if product is not None:
#         product_data = {
#             'id': product.id,
#             'name': product.name,
#             'description': product.description,
#             'price': product.price,
#             'created': product.created_at
#         }

#         return jsonify({'product': product_data})
#     else:
#         return jsonify({'error': 'Product not found'}), 404

if __name__ == "__main__":
    app.run(debug=True, port=8000)
