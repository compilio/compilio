class SessionMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if not request.session.session_key:
            request.session.save()
            request.session.modified = True

        return response
