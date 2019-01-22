from app.views.redflag_views import IncidentViewMap
# from app.views.intervention_views import InterventionViewMap
from app import app

# endpoints for the redflag incident
route_url_create = IncidentViewMap.as_view('create')
app.add_url_rule('/api/v1/red-flags',
                    view_func=route_url_create, methods=['POST',])

route_url_get_all = IncidentViewMap.as_view('get_all')
app.add_url_rule('/api/v1/red-flags', defaults = None, 
                    view_func=route_url_get_all, methods=['GET',])

route_url_get_one = IncidentViewMap.as_view('get_one')
app.add_url_rule('/api/v1/red-flags/<int:id>',defaults = None, 
                    view_func=route_url_get_one, methods=['GET',])

route_url_delete_one = IncidentViewMap.as_view('delete_one')
app.add_url_rule('/api/v1/red-flags/<int:id>',defaults = None, 
                    view_func=route_url_delete_one, methods=['DELETE',])

route_url_edit_comment = IncidentViewMap.as_view('patch_comment')
app.add_url_rule('/api/v1/red-flags/<int:id>/comment',defaults = None, 
                    view_func=route_url_edit_comment, methods=['PATCH',])

route_url_edit_location = IncidentViewMap.as_view('patch_location')
app.add_url_rule('/api/v1/red-flags/<int:id>/location',defaults = None, 
                    view_func=route_url_edit_location, methods=['PATCH',])


# endpoints for the intervvention incident
# intervention_url = InterventionViewMap.as_view('create_intervention')
# app.add_url_rule('/api/v1/intervention',
#                     view_func=intervention_url, methods=['POST',])

# intervention_url = InterventionViewMap.as_view('get_all_interventions')
# app.add_url_rule('/api/v1/intervention', defaults = None, 
#                     view_func=intervention_url, methods=['GET',])

# intervention_url = InterventionViewMap.as_view('get_one_intervention')
# app.add_url_rule('/api/v1/intervention/<int:id>',defaults = None, 
#                     view_func=intervention_url, methods=['GET',])

# intervention_url = InterventionViewMap.as_view('delete_one_intervention')
# app.add_url_rule('/api/v1/intervention/<int:id>',defaults = None, 
#                     view_func=intervention_url, methods=['DELETE',])

# intervention_url = InterventionViewMap.as_view('patch_comment_intervention')
# app.add_url_rule('/api/v1/intervention/<int:id>/comment',defaults = None, 
#                     view_func=intervention_url, methods=['PATCH',])

# intervention_url = InterventionViewMap.as_view('patch_location_intervention')
# app.add_url_rule('/api/v1/intervention/<int:id>/location',defaults = None, 
#                     view_func=intervention_url, methods=['PATCH',])
