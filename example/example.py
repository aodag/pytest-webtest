def app(environ, start_response):
    start_response(
        "200 OK",
        [('Content-type', 'text/plain;charset=utf-8')])
    return [b"Hello, world!"]


def main(global_conf, **app_conf):
    return app
