from app.views.create_redflag import CreateRedFlagMap
from app import app

route_url_create = CreateRedFlagMap.as_view('create')

app.add_url_rule('/api/v1/redflagrecord', defaults={'id': None},
                 view_func=route_url_create, methods=['POST',])