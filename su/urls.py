
from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r"^(?P<username>.*)/$", views.switch_user, name="su_switch_user"),
]
