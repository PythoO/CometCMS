from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

report_bp = Blueprint('report', __name__, template_folder='templates')


@report_bp.route('/')
def show():
    try:
        return render_template('report_show.html')
    except TemplateNotFound:
        abort(404)
