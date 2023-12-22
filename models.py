from flask import Flask, jsonify
from mongoengine import connect, Document, StringField, EmailField
import atexit

app = Flask(__name__)

db = "mydatabase"
host = "127.0.0.1"
port = 27017

connect(db=db, host=host, port=port)


class Task(Document):
    title = StringField(required=True)
    description = StringField()


@app.route('/create_tasks')
def create_tasks():
    tasks_data = [
        {'title': 'Task 1', 'description': 'Description 1'},
        {'title': 'Task 2', 'description': 'Description 2'},
        {'title': 'Task 3', 'description': 'Description 3'}
    ]

    Task.objects.insert_many(tasks_data)

    return jsonify({'message': 'Tasks created successfully!'})

# Route to get all tasks
@app.route('/get_tasks')
def get_tasks():
    tasks = Task.objects.all()
    task_list = [{'title': task.title, 'description': task.description} for task in tasks]
    return jsonify({'tasks': task_list})

# Close MongoDB connection on application shutdown
@app.before_first_request
def setup():
    atexit.register(lambda: connect.close())

if __name__ == '__main__':
    app.run(debug=True)