
from django.conf.urls import patterns, url


urlpatterns = patterns(
    "su.views",
    url(r"^(?P<username>.*)/$", "switch_user", name="su_switch_user"),
)
