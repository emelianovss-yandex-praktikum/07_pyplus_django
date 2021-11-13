from wsgiref.simple_server import make_server


def application(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return [b'Hello world']


with make_server('', 8000, application) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()
