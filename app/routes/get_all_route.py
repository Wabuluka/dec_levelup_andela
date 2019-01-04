from app.views.get_all_view import GetAllCorruptionMap
from app import app

route_url_all = GetAllCorruptionMap.as_view('route_url')

app.add_url_rule('/api/v1/redflagrecords', defaults={'id': None},
                 view_func=route_url_all, methods=['GET',])