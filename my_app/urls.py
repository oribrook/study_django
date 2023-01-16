from django.urls import path
# import my_app.views
from . import views

urlpatterns = [
    # path("home", my_app.views.my_view),
    path("home", views.my_view),
    path("html", views.serve_html),
    path("hello/<str:my_arg>", views.say_hi),

    path("", views.default)
]
