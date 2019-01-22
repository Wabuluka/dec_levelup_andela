from app.views.user_views import CreateNewUser, SigninUser
from app import app

route_url_create_new_user = CreateNewUser.as_view('new_user')
app.add_url_rule('/api/v2/auth/signup',
                 view_func=route_url_create_new_user, methods=['POST',])


route_url_signin = SigninUser.as_view('login')
app.add_url_rule('/api/v2/auth/signin',
                 view_func=route_url_signin, methods=['POST','GET'])