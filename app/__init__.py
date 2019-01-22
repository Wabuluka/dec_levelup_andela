from flask import Flask
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'daviesyoooo'
JWTManager(app)


from app.routes.incident_routes import route_url_create
from app.routes.incident_routes import route_url_get_all
from app.routes.incident_routes import route_url_get_one
from app.routes.incident_routes import route_url_delete_one
from app.routes.incident_routes import route_url_edit_comment
from app.routes.incident_routes import route_url_edit_location
from app.routes.incident_routes import intervention_url

from app.routes.user_routes import route_url_create_new_user
from app.routes.user_routes import route_url_signin