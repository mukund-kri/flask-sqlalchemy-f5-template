from flask.ext.script import Command

from models import db, SimpleModel


class SampleDataCommand(Command):
    '''Populate sample data to a dev sqlite db. (Only for demo app)'''

    def run(self):
        print('Populating demo sqlite db with sample data')
        
        sm = SimpleModel(app_name="Test App")
        db.session.add(sm)
        db.session.commit()

