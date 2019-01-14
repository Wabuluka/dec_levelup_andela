from app.views.create_redflag import CreateRedFlagMap
from app import app

route_url_delete = CreateRedFlagMap.as_view('delete')

app.add_url_rule('/api/v1/redflagrecords/<int:id>', defaults={'id': None},
                 view_func=route_url_delete, methods=['DELETE',])