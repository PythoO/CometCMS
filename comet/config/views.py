from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

config_bp = Blueprint('config', __name__, template_folder='templates')


@config_bp.route('/')
def show():
    try:
        return render_template('config_show.html')
    except TemplateNotFound:
        abort(404)
