from flask import Flask

app = Flask(__name__)

from app.routes.get_all_route import route_url_all
from app.routes.create_redflag_route import route_url_create
# from app.routes.create_case_route import route_url_post