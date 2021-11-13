from urllib.parse import parse_qs
from wsgiref.simple_server import make_server


def auth_middleware(environ):
    query = parse_qs(environ["QUERY_STRING"])
    user = query.get("token")
    if user:
        return {"user": user[0]}, None
    else:
        return [], '401 Unauthorized'


def response_middleware(result, error, start_response):
    if error:
        status = error
        result = [b'Error']
    else:
        status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return result


def handler(data):
    return [b'Hello %s' % data["user"].encode()]


def application(environ, start_response):
    result, error = auth_middleware(environ)
    if not error:
        result = handler(result)
    return response_middleware(result, error, start_response)


with make_server('', 8000, application) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()