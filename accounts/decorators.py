from functools import wraps

from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect


def superuser_required(view_func):
    """Allow authenticated superusers to change data; all others remain read-only."""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        if not request.user.is_superuser:
            raise PermissionDenied("Only superusers can add, update, or delete content.")
        return view_func(request, *args, **kwargs)

    return wrapper
