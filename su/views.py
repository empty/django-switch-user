
from django.http import HttpResponseRedirect, Http404

from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def switch_user(request, username):
    if request.user.is_superuser:
        try:
            user = get_user_model().objects.get(username=username)
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            from_url = request.META.get("HTTP_ORIGIN", "")
            if not from_url:
                from_url = request.META.get("HTTP_HOST", "")
                from_url = from_url and ("http://" + from_url) or "/"
                return HttpResponseRedirect(from_url)
        except User.DoesNotExist:
            pass
    raise Http404
