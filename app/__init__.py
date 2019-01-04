from flask import Flask

app = Flask(__name__)

from app.routes.get_all_route import route_url_all