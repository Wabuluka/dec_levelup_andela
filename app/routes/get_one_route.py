from app.views.create_redflag import CreateRedFlagMap
from app import app

route_url_get_one_redflag = CreateRedFlagMap.as_view('get_one_red_flag')

app.add_url_rule('/api/v1/redflagrecord/<int:id>', defaults={'id': None},
                 view_func=route_url_get_one_redflag, methods=['POST',])