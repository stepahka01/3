
from django.urls import path, include
from .views import raises
from app.views import *

product_patterns = [
    path("", posts),
    path("<int:id>", post),

    path("<int:id>/comments", comments),
    path("<int:id>/likes", likes),

    path("last", last),
    path("popular", popular),
]

urlpatterns = [
    path("about", about),
    path("contacts", contacts),
    path("posts/", include(product_patterns)),
    path("redirect", redirect),
    path("permament", permanent),
    path("set",set),
    path("get",get),
    path("access",access),
    path('raises', raises, name='raises'),
    path("json",json),
    path('set_cookie/', set_cookie, name='set_cookie'),
    path('get_cookie/', get_cookie, name='get_cookie'),

]

