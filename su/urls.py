
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^(?P<username>.*)/$", views.switch_user, name="su_switch_user"),
]
