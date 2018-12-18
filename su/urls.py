
from django.conf.urls import url

import views

urlpatterns = [
    url(r"^(?P<username>.*)/$", views.switch_user, name="su_switch_user"),
]
