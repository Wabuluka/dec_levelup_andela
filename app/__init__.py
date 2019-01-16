from flask import Flask

app = Flask(__name__)

from app.routes.incident_routes import route_url_create, route_url_get_all,route_url_delete_one