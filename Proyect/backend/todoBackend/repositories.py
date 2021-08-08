from todoBackend import db
from todoBackend.models import ToDo

class ToDoRepositorie():

    def addToDatabase(obj):
        db.session.add(obj)
        db.session.commit()
        return 'ok'

    def getAllToDos():
        return ToDo.query.all()

    def deleteToDoFromDatabase(id):
        todo = ToDo.query.get(id)
        db.session.delete(todo)
        db.session.commit()
        return 'ok'

    def updateToDo(id,title):
        todo = ToDo.query.get(id)
        todo.title = title
        db.session.commit()
        return 'ok'

    def complete(id,bol):
        todo = ToDo.query.get(id)
        todo.completed = bol 
        db.session.commit()