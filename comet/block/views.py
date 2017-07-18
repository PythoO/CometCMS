from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
block_bp = Blueprint('block', __name__, template_folder='templates')


@block_bp.route('/', defaults={'page': 'block_show'})
@block_bp.route('/<page>')
def show(page):
    try:
        return render_template('%s.html' % page)
    except TemplateNotFound:
        abort(404)
