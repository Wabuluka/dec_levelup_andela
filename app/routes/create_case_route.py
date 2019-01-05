from app.views.create_view import PostCorruptionMap
from app import app

route_url_post = PostCorruptionMap.as_view('route_url')

app.add_url_rule('/api/v1/red-flags', view_func=route_url_post, methods=['POST',])