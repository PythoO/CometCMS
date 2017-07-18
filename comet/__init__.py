from flask import Flask

from comet.block.views import block_bp
from comet.config.views import config_bp
from comet.content.views import content_bp
from comet.home.views import home_bp
from comet.people.views import people_bp
from comet.report.views import report_bp

from comet.log.comet_log import CometLog

app = Flask(__name__)

app.register_blueprint(block_bp, url_prefix='/admin/block')
app.register_blueprint(config_bp, url_prefix='/admin/config')
app.register_blueprint(content_bp, url_prefix='/admin/content')
app.register_blueprint(home_bp, url_prefix='/admin')
app.register_blueprint(people_bp, url_prefix='/admin/people')
app.register_blueprint(report_bp, url_prefix='/admin/report')
