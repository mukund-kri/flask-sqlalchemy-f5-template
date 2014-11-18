from flask.ext.testing import TestCase

from models import db, SimpleModel


class SimpleModelTest(TestCase):

    
    def create_app(self):
        import app
        return app.create_app('test')


    def setUp(self):
        db.create_all()
        
        a_simple_model = SimpleModel()
        a_simple_model.app_name = "simple_app"

        db.session.add(a_simple_model)
        db.session.commit()


    def test_read_simple_model(self):

        # Get a simple model row by primary key
        sm = SimpleModel.query.get(1)


        assert sm != None
        assert sm.app_name == "simple_app"
