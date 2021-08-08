from todoBackend.models import ToDo
from todoBackend.repositories import  ToDoRepositorie

class ToDoServices():

    def createToDo(title):
        newTODO = ToDo(title)
        ToDoRepositorie.addToDatabase(newTODO)
        return newTODO