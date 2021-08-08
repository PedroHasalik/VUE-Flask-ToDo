from flask import request, jsonify
from flask_marshmallow import Marshmallow
from todoBackend import app
from todoBackend.repositories import  ToDoRepositorie
from todoBackend.services import ToDoServices


ma = Marshmallow(app)

class ToDoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'completed')

todos_schema = ToDoSchema(many=True)

@app.route('/add', methods=['POST'])
def addTODO():
    title = request.json['title']
    newTODO = ToDoServices.createToDo(title)
    return "ToDo created",200

@app.route('/get', methods=[ 'GET' ])
def getTODOS():
    allTodos = ToDoServices. getTodos()
    results  = todos_schema.dump(allTodos)
    return jsonify(results),200

@app.route('/delete/<id>', methods=['DELETE'])
def deleteTODO(id):
    ToDoServices.deleteToDo(id)
    return "ToDo deleted",200


@app.route('/update/<id>', methods=['PUT'])
def updateTODO(id):
    title = request.json['title']
    ToDoServices.updateToDo(id,title)
    return 'ToDo updated',200

@app.route('/complete/<id>', methods=['PUT'])
def completeTODO(id):
    completed = request.json['completed']
    ToDoServices.completeToDo(id,completed)
    return 'ToDo completed',200