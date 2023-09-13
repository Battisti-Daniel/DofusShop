from django.shortcuts import redirect


def not_guest_only(view_func):

    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/home/')
        return view_func(request, *args, **kwargs)

    return wrapper
