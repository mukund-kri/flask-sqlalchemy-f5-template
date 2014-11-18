from flask import Blueprint, render_template
from models import SimpleModel


homebp = Blueprint('home', __name__, template_folder='templates')


@homebp.route('/')
def home():

    sm1 = SimpleModel.query.get(1)
    return render_template("home.html", app_name=sm1.app_name)

