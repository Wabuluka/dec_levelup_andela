from app.views.createviews import CreateViews
from app import app

app.add_url_rule('/api/v1/redflags/', view_func=CreateViews.as_view('create_redflag'),
                         methods=['POST'], strict_slashes=False)