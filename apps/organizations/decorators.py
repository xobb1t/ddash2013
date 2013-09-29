from functools import wraps
from django.http import Http404


def owner_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user = request.user
        organization = request.organization
        if user.is_authenticated() and user.is_owner and \
                organization == user.organization:
            return view_func(request, *args, **kwargs)
        raise Http404
    return _wrapped_view
