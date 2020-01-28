from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options
from tornado.web import Application

from Pickup_action import ActionAnnotator

define('port', default=3002, help='port to listen on')

def main():
    """Construct and serve the tornado application."""

    app = Application(handlers= [
        ('/action', ActionAnnotator),
    ])
    http_server = HTTPServer(app)
    http_server.listen(options.port)
    IOLoop.current().start()

if __name__ == '__main__':
    main()
