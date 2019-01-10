from flask import Flask

from app.routes.get_all_route import route_url_all
from app.routes.create_redflag_route import route_url_create
from app.routes.create_user_route import route_url_create_new_user
from app.routes.get_one_route import route_url_get_one_redflag
from app.routes.delete_route import route_url_delete

app = Flask(__name__)

