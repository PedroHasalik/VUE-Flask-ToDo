from todoBackend.models import ToDo
from todoBackend.repositories import  ToDoRepositorie

class ToDoServices():

    def createToDo(title):
        newTODO = ToDo(title)
        ToDoRepositorie.addToDatabase(newTODO)
        return newTODO

    def getTodos():
        return ToDoRepositorie.getAllToDos()

    def deleteToDo(id):
        return ToDoRepositorie.deleteToDoFromDatabase(id)

    def updateToDo(id,title):
        return ToDoRepositorie.updateToDo(id,title)

    def completeToDo(id,completed):
        return ToDoRepositorie.complete(id,completed)