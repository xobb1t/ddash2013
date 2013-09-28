from django.contrib.auth.decorators import user_passes_test
from django.http import Http404
from django.utils.functional import wraps


def user_is_owner(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user = request.user
        organization = request.organization
        if user.is_owner and organization == request.user.organization:
            return view_func(request, *args, **kwargs)
        raise Http404
    return _wrapped_view
