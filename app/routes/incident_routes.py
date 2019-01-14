from app.views.incident_views import CreateRedFlagMap, GetAllCorruptionMap, GetOneCorruptionMap
from app import app

route_url_create = CreateRedFlagMap.as_view('create')
app.add_url_rule('/api/v1/redflagrecord', defaults={'id': None},
                    view_func=route_url_create, methods=['POST',])

route_url_get_all = GetAllCorruptionMap.as_view('get_all')
app.add_url_rule('/api/v1/redflagrecords', defaults = None, 
                    view_func=route_url_get_all, methods=['GET',])

route_url_get_one = GetOneCorruptionMap.as_view('get_one')
app.add_url_rule('/api/v1/redflagrecords/<int:id>',defaults = None, 
                    view_func=route_url_get_one, methods=['GET',])
