from flask import Flask, Blueprint



app = Flask(__name__)
app.config.from_object('config')

from app.views.user import user
from app.views.redflag import redflag
from app.views.intervention import intervention
from app.views.admin import admin

app.register_blueprint(user, url_prefix = '/api/v2/auth/')
app.register_blueprint(redflag, url_prefix = '/api/v2/')
app.register_blueprint(intervention, url_prefix = '/api/v2/')
app.register_blueprint(admin, url_prefix = '/api/v2/admin/')