from app.views.user_views import CreateNewUser
from app import app

route_url_create_new_user = CreateNewUser.as_view('new_user')
app.add_url_rule('/api/v1/user', defaults={'id': None},
                 view_func=route_url_create_new_user, methods=['POST',])