from flask import Blueprint, render_template, abort, flash, request, redirect, url_for, current_app
from jinja2 import TemplateNotFound

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

import logging
import re

config_bp = Blueprint('config', __name__, template_folder='templates')

class ConfigForm(FlaskForm):
    site_name = StringField('Site Name', validators=[DataRequired()])
    email_address = StringField('Email address', validators=[DataRequired()])


@config_bp.route('/', methods=['GET', 'POST'])
def show():
    try:
        logging.info('This message should go to the log file')
        return render_template('config_show.html')
    except TemplateNotFound:
        abort(404)


@config_bp.route('/system/basic', methods=['GET', 'POST'])
def system():
    try:
        form = ConfigForm()
        if request.method == 'POST':
            msg = 'Configuration successfully saved.'
            flash(msg, 'success')
            logging.info(msg)
            return redirect(url_for('config.show'))
        return render_template('config_system.html', form=form)
    except TemplateNotFound:
        abort(404)


@config_bp.route('/development/clearcache', methods=['GET', 'POST'])
def clear_cache():
    try:
        msg = 'Cache successfully clear.'
        flash(msg, 'success')
        logging.info(msg)
        return render_template('config_show.html')
    except TemplateNotFound:
        abort(404)

@config_bp.route('/development/log')
def log():
    try:
        logs = []
        file = open('comet.log', 'r')
        for line in file.readlines():
            date, category, msg = re.split(r'::', line)
            logs.append([date.strip(), category.strip(), msg.strip()])
        logs = logs[::-1]
        file.close()
        return render_template('config_log.html', logs=logs)
    except TemplateNotFound:
        abort(404)

@config_bp.route('/development/log/clear')
def clear_log():
    try:
        logs = []
        file = open('comet.log', 'w')
        file.close()
        return redirect(url_for('config.log'))
    except TemplateNotFound:
        abort(404)