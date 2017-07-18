from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

content_bp = Blueprint('content', __name__, template_folder='templates')


@content_bp.route('/', defaults={'page': 'content_show'})
@content_bp.route('/<page>')
def show(page):
    try:
        return render_template('%s.html' % page)
    except TemplateNotFound:
        abort(404)
