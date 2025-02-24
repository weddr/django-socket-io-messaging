from django.http import HttpResponseBadRequest


def ajax_required(func):
    def wrapper(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest()
        return func(request, *args, **kwargs)

    return wrapper
