def get_post_data(request, name):
    if name in request.POST:
        return request.POST[name]
    else:
        return None
