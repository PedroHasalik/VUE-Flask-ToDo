from todoBackend import db

class ToDo (db.Model):
    id = db.Column(db.Integer, primary_key=True);
    title = db.Column (db.String(100), nullable=False);
    completed = db.Column (db.Boolean, default=False, nullable=False);

    def __init__(self,title):
        self.title = title