django-switch-user
======================================

Django Switch User is a reuasable application that allows users to assume the
identify of another user. It can be helpful when debugging user issues.

Installation
------------
pip install django-switch-user

Quickstart
----------
After installing Django Switch User you just need to add `su` to `INSTALLED_APPS` and wire it into your urls.

    url(r"^admin/su/", include("su.urls")),

