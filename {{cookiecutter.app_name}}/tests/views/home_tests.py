'''
Tests regarding the home blueprint.
'''

from flask import Flask
from flask.ext.testing import TestCase

from models import db, SimpleModel


class MainBlueprintTest(TestCase):

    render_templates = False

    def create_app(self):
        import app
        return app.create_app('test')


    def setUp(self):
        db.create_all()
        a_simple_model = SimpleModel()
        a_simple_model.app_name = "simple_app"

        db.session.add(a_simple_model)
        db.session.commit()


    def test_home_page(self):
        response = self.client.get('/')
        assert "" == response.data

        self.assert_template_used('home.html')

        name = self.get_context_variable("app_name")
        assert name == "simple_app"
