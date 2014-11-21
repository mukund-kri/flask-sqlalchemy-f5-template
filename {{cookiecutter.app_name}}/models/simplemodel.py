from models.database import db



class SimpleModel(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    app_name = db.Column(db.String(80))

    def __repr__(self):
        return "<SimpleModel %s>" % (self.app_name)
