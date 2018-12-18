
from django.conf.urls import url

import views

urlpatterns = [
    "su.views",
    url(r"^(?P<username>.*)/$", views.switch_user, name="su_switch_user"),
]
