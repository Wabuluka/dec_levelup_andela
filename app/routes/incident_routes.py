from app.views.incident_views import (CreateRedFlagMap, GetAllCorruptionMap, GetOneCorruptionMap, DeleteRedFlag,
EditStatusMap, EditLocationMap)
from app import app

# route_url_index = CreateRedFlagMap.as_view('index')
# app.add_url_rule('/',
#                     view_func=route_url_index, methods=['GET',])

route_url_create = CreateRedFlagMap.as_view('create')
app.add_url_rule('/api/v1/redflagrecords',
                    view_func=route_url_create, methods=['POST',])

route_url_get_all = GetAllCorruptionMap.as_view('get_all')
app.add_url_rule('/api/v1/redflagrecords', defaults = None, 
                    view_func=route_url_get_all, methods=['GET',])

route_url_get_one = GetOneCorruptionMap.as_view('get_one')
app.add_url_rule('/api/v1/redflagrecords/<int:id>',defaults = None, 
                    view_func=route_url_get_one, methods=['GET',])

route_url_delete_one = DeleteRedFlag.as_view('delete_one')
app.add_url_rule('/api/v1/redflagrecords/<int:id>',defaults = None, 
                    view_func=route_url_delete_one, methods=['DELETE',])

route_url_edit_status = EditStatusMap.as_view('edit_status')
app.add_url_rule('/api/v1/redflagrecords/edit-status/<int:id>',defaults = None, 
                    view_func=route_url_edit_status, methods=['PUT',])


route_url_edit_location = EditLocationMap.as_view('edit_location')
app.add_url_rule('/api/v1/redflagrecords/edit-location/<int:id>',defaults = None, 
                    view_func=route_url_edit_location, methods=['PUT',])


route_url_edit_comment = EditLocationMap.as_view('edit_comment')
app.add_url_rule('/api/v1/redflagrecords/edit-comment/<int:id>',defaults = None, 
                    view_func=route_url_edit_comment, methods=['PUT',])