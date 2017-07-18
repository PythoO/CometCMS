from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

people_bp = Blueprint('people', __name__, template_folder='templates')


@people_bp.route('/')
def show():
    try:
        return render_template('people_show.html')
    except TemplateNotFound:
        abort(404)
